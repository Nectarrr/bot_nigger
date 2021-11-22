import telebot
from telebot import types

token='2137014095:AAFhyonMOrkB9DFjoj4Fh3O7dXqgMAcvTzw'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Покажи данные по дому":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    elif message.text=="Кухня":
        bot.send_message(message.chat.id,'Пидор')
    elif message.text=="Гостинная":
        bot.send_message(message.chat.id, 'Лох')

bot.infinity_polling()