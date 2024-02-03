import requests
from pprint import pprint as print
import telebot

# sura = 2
# oyat = 35

# url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
# url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
bot = telebot.TeleBot(token="BOT_TOKEN")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu aleykum bu bot orqali qurondagi oyat va suralarni o'qish mumkin\nNechinchi Sura o'qimoqchisiz sonini kiriting\n\nMasalan: 1")

@bot.message_handler(func=lambda message: True)
def get_sura(message):
    try:
        user_msg = int(message.text)
        bot.send_message(message.chat.id, "Oyat sonini kiriting\n\nMasalan: 3")
        bot.register_next_step_handler(message, get_oyat, user_msg)
    except ValueError:
        bot.send_message(message.chat.id, "Noto'g'ri son kiritdingiz. Faqat raqamlarni kiriting.")

def get_oyat(message, user_msg):
    try:
        tafsir = 'uzb-muhammadsodikmu'
        user_nrg = int(message.text)
        url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{user_msg}.json"
        url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{user_msg}/{user_nrg}.json"
        r = requests.get(url_oyat)
        print(r.status_code)
        res = r.json()
        x = res['text']
        bot.send_message(message.chat.id, f"Oyat: {x}")
    except ValueError:
        bot.send_message(message.chat.id, "Noto'g'ri son kiritdingiz. Faqat raqamlarni kiriting.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
