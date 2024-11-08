from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from modules.logging import logging
import os, json



load_dotenv();APP_TOKEN, BOT_LANGUAGE = os.getenv("APP_TOKEN"), os.getenv("BOT_LANGUAGE")

if APP_TOKEN is None or BOT_LANGUAGE is None or APP_TOKEN == "default" or BOT_LANGUAGE == "default":
    exit("Error: APP_TOKEN or BOT_LANGUAGE is blank or default")


global localeFile

try:
    localeFile = json.load(open(f"locales/{BOT_LANGUAGE}.json"))
except FileNotFoundError:
    exit(f"Error: {BOT_LANGUAGE}.json not found in locales directory")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"{update.effective_user.first_name} used /hello")
    await update.message.reply_text(localeFile["hello"]["response"])

app = ApplicationBuilder().token(APP_TOKEN).build()
app.add_handler(CommandHandler("hello", hello))

if __name__ == "__main__":
    logging("BOT is running")
    app.run_polling()