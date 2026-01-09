import os
import sys
import telebot
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as e:
    print("Failed to load .env file")
    print(e)
    sys.exit(1)

try:
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing or empty")

except Exception as e:
    print("BOT_TOKEN error:")
    print(e)
    sys.exit(1)


try:
    bot = telebot.TeleBot(BOT_TOKEN)
except Exception as e:
    print("Failed to initialize Telegram bot")
    print(e)
    sys.exit(1)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    try:
        bot.reply_to(message, "How are you doing?")
    except Exception as e:
        print("Error sending welcome message:", e)


@bot.message_handler(commands=["amir"])
def msg(message):
    try:
        bot.reply_to(message, "amir! the smart one")
    except Exception as e:
        print("Error replying to message:", e)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        bot.reply_to(message, message.text)
    except Exception as e:
        print("Error replying to message:", e)



try:
    print(" Bot is running...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

except KeyboardInterrupt:
    print("\n Bot stopped manually")

except Exception as e:
    print("Bot polling error:", e)

