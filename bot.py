from webbrowser import get
import telebot;
from pall import pall;
from fp import fp;
from fc import fc;

bot = telebot.TeleBot('5111904045:AAF1DGUSp6MZSRIYVqZgGEcjawohPvcaNL8');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Доброго времени суток, чем я могу тебе помочь? \n Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Чат бот в Telegram для поиска подработки для несовершеннолетних. \n Список команд: \n /l - получить список всех вакансий;"\
            "\n /fp \"название метро\" поиск вакансии по ближайшему метро; "\
            "\n /fc \"минимальная стоимость\" \"максимальная стоимость\" ")
    elif str(message.text).lower() == "/l":
        # print(message.chat.id)
        bot.send_message(message.from_user.id, pall())
    elif splitted_text[0] == "/fp":
        if len(splitted_text)>1:
            bot.send_message(message.from_user.id,  fp(splitted_text[1]))    
    elif splitted_text[0] == "/fc":
        if len(splitted_text)>1:
            bot.send_message(message.from_user.id,  fc(splitted_text[1], splitted_text[2]))
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")

bot.polling(none_stop=True, interval=0)