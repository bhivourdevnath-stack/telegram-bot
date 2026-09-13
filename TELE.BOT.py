import os
import sys
import telebot
from config import Name
from dotenv import load_dotenv
import ai_int
import traceback



# This part loads environment variables from the .env file (mostly for api key)
# It helps keep secret values like the Telegram bot token safe and other api key.
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

# Get the OpenRouter API key from the environment.
try:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is missing or empty")

except Exception as e:
    print("OPENROUTER_API_KEY error:")
    print(e)
    sys.exit(1)

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



# This command is triggered when the user sends /start or /hello.
@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, f"How are you doing? Feel free to ask me anything about {Name}!")
    # This command sends a simple greeting when the user starts the bot.



#you can add more commands here if you want to expand the bot's functionality.
#just follow the same pattern as the /start and /help commands above.

@bot.message_handler(commands=["help", "commands"])
def show_help(message):
    try:
        bot.reply_to(message, HELP_TEXT)
    except Exception as e:
        print("Error sending help message:", e)


# This is the main message handler(you get the message from the ai)
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



print(" Bot is running...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)

