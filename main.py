import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, ContextTypes, CommandHandler,
    CallbackQueryHandler
)
from config import BOT_TOKEN, WEBHOOK_URL
from database import init_db

app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()

@app.route("/", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"

# Команда /start — выбор языка
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton("🇺🇿 O‘zbek", callback_data="lang_uz")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Привет! Выберите язык:", reply_markup=reply_markup)

# Обработка выбора языка
async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "lang_ru":
        await query.edit_message_text("🇷🇺 Язык установлен: Русский\n📂 Выберите раздел:")
        # тут потом покажем список разделов
    elif query.data == "lang_uz":
        await query.edit_message_text("🇺🇿 Til tanlandi: O‘zbek\n📂 Bo‘limni tanlang:")
        # тут потом покажем список разделов

if __name__ == "__main__":
    init_db()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(language_callback, pattern="^lang_"))

    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL
    )
