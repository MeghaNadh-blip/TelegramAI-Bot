import os

from dotenv import load_dotenv

from telegram import Update

from telegram.ext import (
    ApplicationBuilder, 
    ContextTypes , 
    MessageHandler, 
    filters
)

from autogen import AssistantAgent

#load env file to main program
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#  Groq LLM configuration

llm_config = {
    "config_list":[
        {
            "model": "llama-3.1-8b-instant",
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1",
            "price":[0,0]
        }

    ],
    "temperature": 0.7,
}

# Thinker Agent 

thinker= AssistantAgent(
    name="Thinker",
    llm_config=llm_config,
    system_message="Analyze the user message and provide a detailed analysis with the provided context ."

)

#Writer Agent
writer=AssistantAgent(
    name="Writter",
    llm_config=llm_config,
    system_message="Based on the user message and the analysis provided by thinker agent, generate a concise and relevant response to the user."
)

#cbatbot Function
async def chatbox(
        update:Update,
        context:ContextTypes.DEFAULT_TYPE
):
    #user message
    user_message=update.message.text
    print("User message ")
    print(user_message)

    #thinker agent response
    
    analysis=thinker.generate_reply(
        messages=[
            {
                "role":"user",
                "content":user_message
            }
        ]
    )
    print("\nThinker response ")
    print(analysis)


    #writer agent response

    reply=writer.generate_reply(
        messages=[
            {
                "role":"user",
                "content":f"""
                User message: {user_message}
                Analysis: {analysis}
                """
            }
        ]
    )
    print("\nWriter response ")
    print(reply)

    #Telegram bot reply

    await update.message.reply_text(
        str(reply)
    )

#Telegram App

app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        chatbox
    )
)   

print("Bot is running...")
app.run_polling()