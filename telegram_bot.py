import logging
import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from core import get_bot_reply

TOKEN = "8321922876:AAGjp-n0mCpHET0ccSuYrRj_Gue9zT7cuT0"

logging.basicConfig(level=logging.INFO)

async def handle_message(update, context):
    text = update.message.text
    reply = get_bot_reply(text)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot berjalan...")
app.run_polling()
