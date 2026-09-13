# AI Telegram Bot

A beginner-friendly Telegram bot that answers questions about you using an AI model through [OpenRouter](https://openrouter.ai/).

You can use this project as a starting point instead of building a Telegram bot from the beginning. The bot already includes:

- Telegram message handling
- `/start` and `/hello` commands
- `/help` and `/commands` commands
- OpenRouter AI integration
- Fallback AI models if the main model is unavailable
- Personal information configuration through `user_config.py`
- Basic tests for the AI request payload

This guide explains exactly how to copy this project from GitHub and run it on your own computer. You do not need to build the Telegram connection from the beginning. Deployment instructions are intentionally not included.

## Beginner Quick Start

Follow these steps in order. Do not skip the steps for creating the two API keys.

```powershell
git clone https://github.com/bhivourdevnath-stack/telegram-bot.git
cd telegram_botv1
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

After that, create `.env`, add your Telegram and OpenRouter keys, edit `user_config.py`, and start the bot:

```powershell
python -m unittest test_ai_int.py
python TELE.BOT.py
```

The detailed instructions below explain every command and where to get the keys.

## How the Bot Works

The bot follows this path when someone sends a normal message:

1. Telegram receives the message.
2. `TELE.BOT.py` passes the message to `ai_int.py`.
3. `ai_int.py` converts the Telegram message into plain text.
4. The bot adds your personal information and instructions from `config.py` and `user_config.py`.
5. The request is sent to OpenRouter.
6. OpenRouter returns an AI response.
7. The bot sends the response back to Telegram.

The personal information is included in the AI system prompt, so the AI can answer questions about you as your personal AI representative.

## Requirements

Before starting, install:

- Python 3.10 or newer
- Git
- VS Code, or another code editor
- A Telegram account
- An OpenRouter account
- Internet access

You do not need to know how to build a Telegram bot from scratch. Basic command-line familiarity is enough. If you do not have Git, install it from [git-scm.com](https://git-scm.com/downloads). If you do not have Python, install it from [python.org](https://www.python.org/downloads/) and select **Add Python to PATH** during installation.

## Project Files

| File | Purpose |
| --- | --- |
| `TELE.BOT.py` | Starts the Telegram bot and handles Telegram messages and commands. |
| `ai_int.py` | Sends user messages to OpenRouter and returns the AI response. |
| `config.py` | Builds the AI system prompt using your information. |
| `user_config.py` | The file where you enter your name and personal information. |
| `requirements.txt` | Lists the Python packages required by the project. |
| `test_ai_int.py` | Tests input normalization and payload creation. |
| `.env` | Stores secret keys on your computer. Do not share or commit this file. |
| `.env.example` | Example environment variable names. |
| `Procfile.txt` | Deployment-related configuration. It is not needed for this local setup. |

## Step 1: Clone the Project from GitHub

Cloning means downloading a copy of the project from GitHub to your computer.

1. Open PowerShell. On Windows, press the Windows key, type `PowerShell`, and open it.
2. Move to the folder where you want to keep the project. For example:

```powershell
cd $HOME\Documents
```

3. Clone the repository:

```powershell
git clone https://github.com/bhivourdevnath-stack/telegram_botv1.git
```

4. Enter the new project folder:

```powershell
cd telegram_bot
```

5. Confirm that the project files were downloaded:

```powershell
Get-ChildItem
```

You should see files such as `TELE.BOT.py`, `ai_int.py`, `user_config.py`, and `requirements.txt`.

You can now open the project in VS Code with:

```powershell
code .
```

If `code .` is not recognized, open VS Code normally, choose **File > Open Folder**, and select the `telegram_botv1` folder.

From this point onward, run every command in the terminal opened inside the `telegram_botv1` folder.

## Step 2: Create a Virtual Environment

A virtual environment keeps this bot's packages separate from other Python projects.

Run:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in PowerShell as your user account, then try activation again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

When the environment is active, you should see `.venv` at the beginning of the terminal prompt.

If you close the terminal and open it again later, activate the environment again before running the bot:

```powershell
cd $HOME\Documents\telegram_botv1
.venv\Scripts\Activate.ps1
```

## Step 3: Install the Required Packages

With the virtual environment activated, run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The project uses:

- `pyTelegramBotAPI` to communicate with Telegram
- `python-dotenv` to read values from `.env`
- `requests` to send requests to OpenRouter

If `requests` is not installed by your current `requirements.txt`, install it directly:

```powershell
python -m pip install requests
```

## Step 4: Create a Telegram Bot and Get the Telegram Token

Telegram bots are created and managed through the official **BotFather** account.

1. Open Telegram.
2. Search for `@BotFather`.
3. Open the account with the official verification mark.
4. Send `/start`.
5. Send `/newbot`.
6. Enter a display name for your bot, such as `Bivour AI Representative`.
7. Enter a username for your bot. The username must end in `bot`, for example, `bivour_ai_bot`.
8. BotFather will reply with an HTTP API token.
9. Copy that token and keep it private.

The token usually looks similar to this:

```text
123456789:AAExampleTelegramToken
```

Do not publish this token. Anyone who has it may control your bot.

## Step 5: Create an OpenRouter API Key

OpenRouter provides access to the AI models used by this project.

1. Go to [openrouter.ai](https://openrouter.ai/).
2. Create an account or sign in.
3. Open the **Keys** or **API Keys** section in your dashboard.
4. Choose the option to create a new key.
5. Give the key a recognizable name, such as `telegram-ai-bot`.
6. Copy the key immediately and keep it private.

An OpenRouter key usually starts with `sk-or-`.

Depending on the model and your account, OpenRouter may require credits or have usage limits. The bot currently uses free model identifiers, but availability and rate limits can change.

## Step 6: Create and Configure `.env`

Go to the file named `.env` in the same folder as `TELE.BOT.py`.

Add these two lines:

```env
BOT_TOKEN=PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE
OPENROUTER_API_KEY=PASTE_YOUR_OPENROUTER_API_KEY_HERE
```

Replace the placeholder values with your real tokens. For example:

```env
BOT_TOKEN=123456789:AAExampleTelegramToken
OPENROUTER_API_KEY=sk-or-example-key
```

Important:

- Do not put spaces around `=`.
- Do not add quotation marks unless your value actually needs them.
- Do not add these values to `user_config.py`.
- Do not send your `.env` file to anyone.
- Do not commit `.env` to GitHub.

The Python code reads the Telegram token using the name `BOT_TOKEN`, not `TELEGRAM_BOT_TOKEN`. If you copy the names from `.env.example`, rename `TELEGRAM_BOT_TOKEN` to `BOT_TOKEN`.

## Step 7: Configure `user_config.py`

Open `user_config.py`. It contains two values:

```python
Name = "Your Name"

Data_about_yourself = """
Write information about yourself here.
"""
```

Replace `Your Name` with your name. Then add useful, truthful information inside the triple quotes.

Example:

```python
Name = "Bivour"

Data_about_yourself = """
I am a Python learner interested in artificial intelligence, backend development,
and Telegram bots. I build small projects to improve my programming skills.

My current skills include Python, basic APIs, Git, and working with AI tools.
My goal is to become better at backend and web development.
"""
```

You can include:

- Your name or preferred name
- Your location, if you want to share it
- Your programming languages and tools
- Your projects
- Your education or learning journey
- Your interests
- Your goals
- Your GitHub work
- Information that you want the AI representative to explain to other people

Do not include passwords, API keys, private addresses, financial information, or anything you do not want to share. The information in this file is sent to the AI provider as part of the system prompt when the bot answers messages.

Keep the information accurate. The bot is instructed not to invent facts, but the quality of its answers depends on the information you provide.

## Step 8: Run the Bot

Make sure:

- Your virtual environment is active.
- The required packages are installed.
- `.env` contains both keys.
- `user_config.py` contains your information.

Start the bot with:

```powershell
python TELE.BOT.py
```

A successful start prints:

```text
Bot is running...
```

Then open Telegram, find the bot username you created, and send `/start`.

Try these commands:

- `/start`
- `/hello`
- `/help`
- `/commands`

You can also send a normal question such as:

```text
What programming languages does Bivour use?
```

To stop the bot, press `Ctrl+C` in the terminal.

## Step 9: Run the Tests

The project includes tests for the parts of the AI integration that do not require an API call.

Run:

```powershell
python -m unittest test_ai_int.py
```

You can also run:

```powershell
python -m unittest discover
```

These tests check that Telegram-style message objects are converted into plain text and that the OpenRouter payload can be serialized as JSON.

## Common Problems

### `BOT_TOKEN is missing or empty`

Check that:

- The file is named `.env`, not `.env.txt`.
- `.env` is in the same folder as `TELE.BOT.py`.
- The variable is named exactly `BOT_TOKEN`.
- The token was copied correctly from BotFather.
- You restarted the bot after changing `.env`.

Correct format:

```env
BOT_TOKEN=your-telegram-token
```

### `Missing OPENROUTER_API_KEY`

Check that the `.env` file contains:

```env
OPENROUTER_API_KEY=your-openrouter-key
```

Also confirm that the key is active in your OpenRouter account.

### `ModuleNotFoundError`

Activate the virtual environment and install the dependencies again:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If the missing module is `requests`, run:

```powershell
python -m pip install requests
```

### The bot starts but does not answer

Check that:

- The terminal still shows the bot running.
- The Telegram token belongs to the correct bot.
- You opened the correct bot chat.
- You pressed **Start** in Telegram.
- Your computer has an internet connection.
- The terminal does not show an OpenRouter error.

### OpenRouter rate-limit or model errors

The bot tries the primary model and then fallback models. OpenRouter model availability can change. Check your OpenRouter dashboard and model availability if every model fails.

### Telegram says that another bot is already using the token

Only one running program should use a bot token at a time. Stop any other copy of the bot before starting this one again.

### `keep_alive` import error

The current local version does not need `keep_alive.py`. If you downloaded an older copy that shows this error, make sure you are using the latest version of the repository and run:

```powershell
git pull
```

This guide does not cover deployment-related keep-alive behavior.

## Security Checklist

- Keep `.env` private.
- Keep your Telegram bot token private.
- Keep your OpenRouter API key private.
- Do not paste tokens into public issues, screenshots, or Git commits.
- Use `.gitignore` to exclude `.env`.
- Only place public, truthful information in `user_config.py`.
- Rotate a key immediately if you accidentally expose it.

## Quick Start

After completing the full setup, the usual workflow is:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest test_ai_int.py
python TELE.BOT.py
```

Your personal AI Telegram bot is ready when the program is running and responds to messages in Telegram.
