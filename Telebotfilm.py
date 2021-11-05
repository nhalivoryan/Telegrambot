import random

import telebot

bot = telebot.TeleBot('2036413742:AAHfvbzGUCScJfMUfVbTVTSZ1yKwLMQNLhQ')

from telebot import types


first = ["https://gidonline.io/film/dzhim-pugovka-i-chyortova-dyuzhina/",
         "https://gidonline.io/film/vo-imya-mesti-2/",
         "https://gidonline.io/film/dyuna-3/",
         "https://gidonline.io/film/otchayannye-aferistki/",
         "https://gidonline.io/film/glavnyj-geroj/"
         "https://gidonline.io/film/el-chapo/"
         "https://gidonline.io/film/xoroshij-ploxoj-kop/"
         "https://gidonline.io/film/kak-poteryat-druzej-i-zastavit-vsex-tebya-nenavidet/"
         "https://gidonline.io/film/dyshi-radi-nas/"
         "https://gidonline.io/film/mstiteli-final/"
         "https://gidonline.io/film/rosomaxa-bessmertnyj/"
         "https://gidonline.io/film/moi-schastlivye-zvezdy-2/"]
second = ["Кино — это сон, то грустный, то смешной. Но всегда прекрасный."]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":

        bot.send_message(message.from_user.id, "Hey, now i will tell you good films.")

        keyboard = types.InlineKeyboardMarkup()

        key_Comedy = types.InlineKeyboardButton(text='Comedy', callback_data='film')
        keyboard.add(key_Comedy)
        key_Thriller = types.InlineKeyboardButton(text='Thriller', callback_data='film')
        keyboard.add(key_Thriller)
        key_Romance = types.InlineKeyboardButton(text='Romance', callback_data='film')
        keyboard.add(key_Romance)
        key_Sport = types.InlineKeyboardButton(text='Sport', callback_data='film')
        keyboard.add(key_Sport)
        key_Drama = types.InlineKeyboardButton(text='Drama', callback_data='film')
        keyboard.add(key_Drama)
        key_Melodrama = types.InlineKeyboardButton(text='Melodrama', callback_data='film')
        keyboard.add(key_Melodrama)
        key_Fantasy = types.InlineKeyboardButton(text='Fantasy', callback_data='film')
        keyboard.add(key_Fantasy)
        key_History = types.InlineKeyboardButton(text='History', callback_data='film')
        keyboard.add(key_History)
        key_Adventure = types.InlineKeyboardButton(text='Adventure', callback_data='film')
        keyboard.add(key_Adventure)
        key_Family = types.InlineKeyboardButton(text='Family', callback_data='film')
        keyboard.add(key_Family)
        key_Crime = types.InlineKeyboardButton(text='Crime', callback_data='film')
        keyboard.add(key_Crime)
        key_Detective = types.InlineKeyboardButton(text='Detective', callback_data='film')
        keyboard.add(key_Detective)

        bot.send_message(message.from_user.id, text='Choose genre!', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write Hello")
    else:
        bot.send_message(message.from_user.id, "I do not understand you. Write /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "film":

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            ' ')

        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
