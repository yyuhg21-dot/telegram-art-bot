from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("8857881134:AAEAKSazklCFdONJMZwCMxE9KyoYaAUUccI")

keyboard = [
    ["📦 Артикули"],
    ["📊 Статистика", "💰 Зарплата"],
    ["📅 Графік"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Вітаю!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "📦 Артикули":
        await update.message.reply_text(
            "Введіть кількість артикулів:"
        )
        return

    await update.message.reply_text(
        f"Отримано: {msg}"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()
