from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8709454218:AAE-zNVfZR7kBvM8wu6Ar_lOvye7f-GO1wQ"

LINK = "https://discord.gg/33ab4Rv33"

WORDS = ["روم", "دس", "ديسكورد"]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if any(word in text for word in WORDS):
        await update.message.reply_text(
            f"رابط الديسكورد 💗\n{LINK}"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

app.run_polling()