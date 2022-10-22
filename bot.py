import telebot
from telebot import types
bot = telebot.TeleBot('5420634070:AAF1mBDyk-mWnVNr9tnTgr60BMQTiVld8Cs')
name = ''
surname = ''
age = ''
d = 0
f = open('ff.txt', 'w')
@bot.message_handler(content_types=['text'])


def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Фамилия + первая буква имени латиницей (Inrobov R)")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Желаемый пароль')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    d = 0
    while d == 0:
        age = message.text
        if surname == age:
            bot.send_message(message.from_user.id, 'Вы зарегистрированы')
            f.write(name)
            f
            f.write(surname)
            f.write("\n n ")

            f.close()

            d = 1
        else:
            bot.send_message(message.from_user.id, 'Неверный пароль')

bot.polling(none_stop=True, interval=0)

