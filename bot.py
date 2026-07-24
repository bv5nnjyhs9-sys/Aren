from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "حطي_توكن_البوت_هنا"
LINK = "حطي_رابط_القروب_او_الروم_هنا"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "روم" in text or "ديسكورد" in text:
        await update.message.reply_text(
            f"هذا الرابط 💗\n{LINK}"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

app.run_polling()
