import os
import sys
import telebot
from keep_alive import keep_alive
from dotenv import load_dotenv
import ai_int
import traceback

# ======= Basic setup =======
# This part loads environment variables from the .env file.
# It helps keep secret values like the Telegram bot token safe.
try:
    load_dotenv()
except Exception as e:
    print("Failed to load .env file")
    print(e)
    sys.exit(1)

# Get the bot token from the environment.
# If it is missing, the program stops to prevent a broken bot.
try:
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing or empty")

except Exception as e:
    print("BOT_TOKEN error:")
    print(e)
    sys.exit(1)

# Create the Telegram bot object.
# This object is what receives messages and sends replies.
try:
    bot = telebot.TeleBot(BOT_TOKEN)
except Exception as e:
    print("Failed to initialize Telegram bot")
    print(e)
    sys.exit(1)

HELP_TEXT = """
Here are the available commands:

/start or /hello - shows a welcome message
/help or /commands - shows this explanation

Any normal message you send is sent to the AI assistant.
The AI replies with a text answer.
"""


# ======= Command handlers =======
# Each function below listens for a specific Telegram command.
# Telegram calls these functions automatically when the user sends a command.

@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    # This command sends a simple greeting when the user starts the bot.
    bot.reply_to(message, "How are you doing? Feel free to ask me anything about Bivour!")



@bot.message_handler(commands=["help", "commands"])
def show_help(message):
    # This command explains what the bot can do.
    try:
        bot.reply_to(message, HELP_TEXT)
    except Exception as e:
        print("Error sending help message:", e)


# This is the main message handler.
# It catches every normal text message that is not a command.
# The message text is then sent to the AI module.
@bot.message_handler(func=lambda message: True)
def message(message):
    try:
        print(f"Received message: {message.text}")
        
        # ai_int.main(message) returns two values: reasoning and final answer.
        # We only need the final text for Telegram.
        _, ai_text = ai_int.main(message)
        
        print(f"AI Response: {ai_text}")
        bot.reply_to(message, ai_text)
        
    except Exception as e:
        error_msg = f"Error generating AI reply: {str(e)}"
        print(error_msg)
        print("Full traceback:")
        traceback.print_exc()
        
        # Send user a more detailed error message
        bot.reply_to(message, f"Sorry, I hit an error: {str(e)[:100]}")


# ======= Bot startup =======
# This line starts the bot and keeps it running in polling mode.
# Polling means the bot keeps checking Telegram for new messages.
print(" Bot is running...")
keep_alive()
bot.infinity_polling(timeout=10, long_polling_timeout=5)

