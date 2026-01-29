import logging
import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from core import get_bot_reply

# =====================
# LOGGING
# =====================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================
# AMBIL TOKEN DARI ENV
# =====================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset")

# =====================
# HANDLER
# =====================
async def handle_message(update, context):
    if not update.message or not update.message.text:
        return

    text = update.message.text
    reply = get_bot_reply(text)
    await update.message.reply_text(reply)

# =====================
# MAIN
# =====================
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("🤖 Bot Telegram berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
