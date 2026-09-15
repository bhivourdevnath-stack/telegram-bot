<p align="center">
  <img src="https://raw.githubusercontent.com/bhivourdevnath-stack/py-test/refs/heads/main/tele.svg" alt="hero.svg">
</p>

<h1></h1><br>

## About


Telegram-bot is a beginner-friendly, AI-powered Telegram bot designed to answer questions about you by acting as your personal AI representative. Built with Python, it integrates seamlessly with Telegram and OpenRouter's AI models to provide intelligent, context-aware responses.

## What It Does

The bot receives messages via Telegram, combines them with your personal information, sends them to OpenRouter's AI service, and returns generated responses—all without requiring you to build the Telegram connection from scratch.

##

<p align="center">
 <img width="1503" height="914" alt="image" src="https://github.com/user-attachments/assets/c62ce394-606c-49ad-8394-3977db24ba70" />
</p>

##  Table of Contents

- [Features](https://github.com/bhivourdevnath-stack/telegram-bot#-features)
- [Quick Start](https://github.com/bhivourdevnath-stack/telegram-bot#-quick-start)
- [How It Works](https://github.com/bhivourdevnath-stack/telegram-bot#-how-it-works)
- [Prerequisites](https://github.com/bhivourdevnath-stack/telegram-bot#-prerequisites)
- [Installation Guide](https://github.com/bhivourdevnath-stack/telegram-bot#-installation-guide)
- [Configuration](https://github.com/bhivourdevnath-stack/telegram-bot#%EF%B8%8F-configuration)
- [Project Structure](https://github.com/bhivourdevnath-stack/telegram-bot#-project-structure)
- [Testing](https://github.com/bhivourdevnath-stack/telegram-bot#-testing)
- [Troubleshooting](https://github.com/bhivourdevnath-stack/telegram-bot#-troubleshooting)
- [Security](https://github.com/bhivourdevnath-stack/telegram-bot#-security-checklist)

---

##  Features

- **Pre-built Telegram Integration** - Message handling and commands ready to use
- **AI-Powered Responses** - Answers questions about you via OpenRouter
- **Easy Setup** - No need to build Telegram connection from scratch
- **Fallback Models** - Alternative AI models if primary is unavailable
- **Personal Configuration** - Customize bot behavior with `user_config.py`
- **Testing Included** - Unit tests for AI payload creation
- **Commands Supported**:
  - `/start` - Initialize the bot
  - `/hello` - Greeting message
  - `/help` - Display available commands
  - `/commands` - List all commands

---

##  Quick Start

### For Windows PowerShell:

```powershell
# Clone the repository
git clone https://github.com/bhivourdevnath-stack/telegram-bot.git
cd telegram_botv1

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Configure your keys and info (see Configuration section)
# Then run:
python -m unittest test_ai_int.py
python TELE.BOT.py
```

---

##  How It Works

```
User Message
    ↓
Telegram receives message
    ↓
TELE.BOT.py → ai_int.py
    ↓
Message converted to plain text
    ↓
Add personal info from user_config.py + config.py
    ↓
Send request to OpenRouter
    ↓
AI generates response
    ↓
Response sent back to Telegram
    ↓
User receives answer
```

The personal information is included in the AI system prompt, so the bot acts as your personal AI representative.

---

##  Prerequisites

Before you start, ensure you have:

- **Python 3.10+** ([download](https://www.python.org/downloads/))
- **Git** ([download](https://git-scm.com/downloads))
- **Code Editor** - VS Code recommended
- **Telegram Account** - To create and test the bot
- **OpenRouter Account** - For AI model access
- **Internet Connection** - Required for API calls

No prior experience building Telegram bots needed—basic command-line familiarity is enough.

---

##  Installation Guide

### Step 1: Clone the Repository

Open PowerShell and run:

```powershell
# Navigate to your desired folder
# Give the folder location where you want to save the project 
cd $HOME\Documents

# Clone the project
git clone https://github.com/bhivourdevnath-stack/telegram-bot.git
cd telegram_bot

# View project files
Get-ChildItem

# Open in VS Code
code .
```

**Note:** If `code .` doesn't work, open VS Code manually → **File > Open Folder** → select the `telegram_bot` folder.

**Note:** If you're new to PowerShell, you can do it directly in VS Code, but I recommend doing it in PowerShell because it's fast, and in the future, if you want to be a programmer, then you have to know those normal PowerShell commands


---

### Step 2: Create and Activate Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate it (PowerShell)
.venv\Scripts\Activate.ps1

# If activation is blocked, run this once:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Note:** You'll see `.venv` in your terminal prompt when active. Reactivate after closing the terminal:

```powershell
cd $HOME\Documents\telegram_bot
.venv\Scripts\Activate.ps1
```

---

### Step 3: Install Dependencies

With the virtual environment active:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Packages installed:**
- `pyTelegramBotAPI` - Telegram communication
- `python-dotenv` - Environment variables
- `requests` - HTTP requests to OpenRouter

---

### Step 4: Create Telegram Bot Token

<p align="center">
<img width="1440" height="921" alt="image" src="https://github.com/user-attachments/assets/322c28ef-d862-40a0-8303-5ddbafacc94f" />
</p>

1. Open **Telegram**
2. Search for [**@BotFather**](https://t.me/botfather) (official verified account)
3. Send `/start`
4. Send `/newbot`
5. Enter a display name (e.g., `Bivour AI Representative`)
6. Enter a username ending in `bot` (e.g., `bivour_ai_bot`)
7. Copy the token returned (format: `123456789:AAExampleToken`)
<img width="895" height="415" alt="image" src="https://github.com/user-attachments/assets/c04b584a-bbcf-490f-866d-0b655f0587ae" />

**Keep this token private!**

---

### Step 5: Create OpenRouter API Key

1. Go to [openrouter.ai](https://openrouter.ai/)
2. Sign up or log in
3. Navigate to **Keys** or **API Keys** in your dashboard 
<img width="920" height="717" alt="image" src="https://github.com/user-attachments/assets/8ba7dbfa-a14b-40d9-a590-de80007009ee" />

4. Create a new key (name it `telegram-ai-bot`)
5. Copy immediately (format: `sk-or-...`)
<img width="589" height="319" alt="image" src="https://github.com/user-attachments/assets/d5a8f94d-a8c1-4350-9451-8e838f525cba" />


**Note:** Depending on your account, OpenRouter may require credits or have usage limits.

---

## ⚙️ Configuration

### Step 6: Create `.env` File

Create a file named `.env` in the project root (same folder as `TELE.BOT.py`):

```env
BOT_TOKEN=123456789:AAExampleTelegramToken
OPENROUTER_API_KEY=sk-or-example-key
```

**Important:**
- ✅ No spaces around `=`
- ✅ No quotation marks (unless your value contains them)
- ❌ Never commit `.env` to GitHub
- ❌ Never share this file
- ❌ Never paste tokens in public issues or screenshots

**Note:** The code reads `BOT_TOKEN`, not `TELEGRAM_BOT_TOKEN`. Update accordingly if copying from `.env.example`.

---

### Step 7: Configure `user_config.py`

Open `user_config.py` and update:

```python
Name = "Your Name"

Data_about_yourself = """
Write information about yourself here.
"""
```

**Example:**

```python
Name = "Bivour"

Data_about_yourself = """
I am a Python learner interested in artificial intelligence, backend development,
and Telegram bots. I build small projects to improve my programming skills.

My current skills include Python, basic APIs, Git, and working with AI tools.
My goal is to become better at backend and web development.
"""
```

**What to include:**
- ✅ Your name or preferred name
- ✅ Programming languages and skills
- ✅ Projects you've built
- ✅ Your interests and goals
- ✅ Learning journey or education
- ✅ GitHub work

**What to exclude:**
- ❌ Passwords or API keys
- ❌ Private addresses or phone numbers
- ❌ Financial information
- ❌ Anything you don't want to share publicly

Keep information **accurate and truthful** for better AI responses.

---

##  Project Structure

| File | Purpose |
|------|---------|
| `TELE.BOT.py` | Main bot script—handles Telegram messages and commands |
| `ai_int.py` | Sends messages to OpenRouter and returns AI responses |
| `config.py` | Builds the AI system prompt from your configuration |
| `user_config.py` | Your personal information (edit this file) |
| `requirements.txt` | Python dependencies |
| `test_ai_int.py` | Unit tests for AI integration |
| `.env` | Secret keys (never commit this) |
| `.env.example` | Example environment variable names |
| `Procfile.txt` | Deployment configuration (not needed for local setup) |

---

##  Testing

Before running the bot, verify the setup with tests:

```powershell
# Run specific test file
python -m unittest test_ai_int.py

# Or discover and run all tests
python -m unittest discover
```

These tests verify:
- Telegram message objects convert to plain text correctly
- OpenRouter payload serializes to valid JSON

---

##  Running the Bot

Ensure all prerequisites are met:

- ✅ Virtual environment is active
- ✅ Dependencies installed
- ✅ `.env` contains both tokens
- ✅ `user_config.py` is configured

**Start the bot:**

```powershell
python TELE.BOT.py
```

Expected output:

```
Bot is running...
```

**Test the bot:**

1. Open Telegram
2. Find your bot username
3. Send `/start`
4. Try commands: `/hello`, `/help`, `/commands`
5. Ask a question: "What programming languages does Bivour use?"

**Stop the bot:** Press `Ctrl+C` in the terminal

---

##  Troubleshooting

### ❌ `BOT_TOKEN is missing or empty`

**Checklist:**
- File is named `.env` (not `.env.txt`)
- `.env` is in the same folder as `TELE.BOT.py`
- Variable is exactly `BOT_TOKEN`
- Token copied correctly from BotFather
- Bot restarted after changing `.env`

**Correct format:**
```env
BOT_TOKEN=123456789:AAYourActualToken
```

---

### ❌ `Missing OPENROUTER_API_KEY`

**Solution:**
```env
OPENROUTER_API_KEY=sk-or-your-actual-key
```

Also verify the key is active in your OpenRouter dashboard.

---

### ❌ `ModuleNotFoundError`

**Solution:**
```powershell
# Reactivate virtual environment
.venv\Scripts\Activate.ps1

# Reinstall dependencies
python -m pip install -r requirements.txt

# If specific module is missing:
python -m pip install requests
```

---

### ❌ Bot starts but doesn't answer

**Checklist:**
- Terminal shows bot still running
- Token belongs to the correct bot
- You opened the correct bot chat
- You pressed **Start** in Telegram
- Computer has internet connection
- No OpenRouter errors in terminal

---

### ❌ OpenRouter model or rate-limit errors

The bot tries the primary model and falls back to alternatives. If all models fail:
- Check your OpenRouter dashboard
- Verify model availability
- Check account credits or limits

---

### ❌ "Another bot is already using the token"

**Solution:** Only one instance can use a token. Stop any other running copies before restarting.

---

##  Security Checklist

- 🔐 Keep `.env` private
- 🔐 Keep Telegram bot token confidential
- 🔐 Keep OpenRouter API key confidential
- 🔐 Never paste tokens in public issues or screenshots
- 🔐 Use `.gitignore` to exclude `.env`
- 🔐 Only use public, truthful information in `user_config.py`
- 🔐 Rotate keys immediately if accidentally exposed

---

##  After Setup: Typical Workflow

```powershell
# Activate environment
.venv\Scripts\Activate.ps1

# Install/update dependencies
python -m pip install -r requirements.txt

# Run tests
python -m unittest test_ai_int.py

# Start bot
python TELE.BOT.py
```

Your personal AI Telegram bot is ready when the program runs and responds to Telegram messages! 🎉

---

##  License



##  Contributing


