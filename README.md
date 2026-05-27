
````markdown
# 🤖 TelegramAI-Bot

An AI-powered Telegram chatbot built using Python and Groq LLM APIs.  
This bot can receive user messages from Telegram and generate intelligent AI responses in real time.

---

## 🚀 Features

- Telegram Bot Integration
- AI Responses using Groq API
- Real-time message handling
- Lightweight and beginner-friendly project
- Easy to customize and extend

---

## 🛠️ Tech Stack

- Python
- python-telegram-bot
- Groq API
- python-dotenv

---

## 📂 Project Structure

```bash
TelegramAI-Bot/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MeghaNadh-blip/TelegramAI-Bot.git
cd TelegramAI-Bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
pip install python-telegram-bot python-dotenv groq
```

---

## 🤖 Creating a Telegram Bot API Token

This project uses the Telegram Bot API to interact with users through Telegram.

### 1️⃣ Open Telegram

Search for:

```text
@BotFather
```

BotFather is the official Telegram bot used to create and manage bots.

---

### 2️⃣ Start BotFather

```text
/start
```

---

### 3️⃣ Create a New Bot

```text
/newbot
```

BotFather will ask for:

- Bot Name
- Unique Username

⚠️ Username must end with `bot`

Example:

```text
AI Assistant
ai_assistant_bot
```

---

### 4️⃣ Copy Your Bot Token

After successful creation, BotFather will generate a token like:

```text
123456789:AAExampleTelegramBotToken
```

⚠️ Keep this token private and never upload it to GitHub.

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

---

## 🔒 Security Best Practices

Ensure `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
```

This prevents sensitive credentials and unnecessary files from being uploaded to GitHub.

---

## ▶️ Run the Bot

```bash
python3 app.py
```

---

## 💡 Future Improvements

- Voice message support
- Image generation
- Conversation memory
- Web search integration
- Cloud deployment

---

## 👨‍💻 Author

**Meghanadh Sai Nalluri**

- GitHub: [https://github.com/MeghaNadh-blip](https://github.com/MeghaNadh-blip)
- LinkedIn: [https://www.linkedin.com/in/meghanadh-nalluri-942b97322/](https://www.linkedin.com/in/meghanadh-nalluri-942b97322/)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
