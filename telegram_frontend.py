# telegram_frontend.py
import telebot
from backend_downloader import download_video   

API_TOKEN = "8342188590:AAFR1c4yQSp1nQvC_aV88WQFoCYtRuOLg-M"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привіт! Надішли мені посилання на YouTube відео, і я його завантажу."
    )

@bot.message_handler(content_types=['text'])
def handle_url(message):
    url = message.text.strip()

    bot.send_message(message.chat.id, "⏳ Завантажую відео...")

    file_path = download_video(url)  

    if file_path:
        bot.send_document(message.chat.id, open(file_path, "rb"))
        bot.send_message(message.chat.id, "✅ Готово!")
    else:
        bot.send_message(message.chat.id, "❌ Помилка під час завантаження.")

bot.polling()
