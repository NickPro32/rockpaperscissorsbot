# @ardotcotbot
import telebot

waiting = False
answer = ''
person = ''
name = ''

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Камень", callback_data="button1")
    button2 = telebot.types.InlineKeyboardButton(text="Ножницы", callback_data="button2")
    button3 = telebot.types.InlineKeyboardButton(text="Бумага", callback_data="button3")
    keyboard.row(button1, button2, button3)
    bot.send_message(message.from_user.id, "Я хочу сыграть с тобой в игру", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(callback_obj: telebot.types.CallbackQuery):
    global waiting
    global answer
    global person
    global name
    if waiting and callback_obj.from_user.id != person:
        if callback_obj.data == 'button1':
            if answer == 'button1':
                bot.send_message(callback_obj.from_user.id, 'Ничья')
                bot.send_message(person, 'Ничья')
            elif answer == 'button3':
                bot.send_message(callback_obj.from_user.id, 'Поражение ' + name + ' оказался удачливее')
                bot.send_message(person, 'Победа. Вам везет больше чем ' + callback_obj.from_user.username)
            else:
                bot.send_message(callback_obj.from_user.id, 'Победа. Вам везет больше чем ' + name)
                bot.send_message(person, 'Поражение. ' + callback_obj.from_user.username + ' оказался удачливее')
        elif callback_obj.data == 'button2':
            if answer == 'button2':
                bot.send_message(callback_obj.from_user.id, 'Ничья')
                bot.send_message(person, 'Ничья')
            elif answer == 'button1':
                bot.send_message(callback_obj.from_user.id, 'Поражение ' + name + ' оказался удачливее')
                bot.send_message(person, 'Победа. Вам везет больше чем ' + callback_obj.from_user.username)
            else:
                bot.send_message(callback_obj.from_user.id, 'Победа. Вам везет больше чем ' + name)
                bot.send_message(person, 'Поражение. ' + callback_obj.from_user.username + ' оказался удачливее')
        elif callback_obj.data == 'button3':
            if answer == 'button3':
                bot.send_message(callback_obj.from_user.id, 'Ничья')
                bot.send_message(person, 'Ничья')
            elif answer == 'button2':
                bot.send_message(callback_obj.from_user.id, 'Поражение ' + name + ' оказался удачливее')
                bot.send_message(person, 'Победа. Вам везет больше чем ' + callback_obj.from_user.username)
            else:
                bot.send_message(callback_obj.from_user.id, 'Победа. Вам везет больше чем ' + name)
                bot.send_message(person, 'Поражение. ' + callback_obj.from_user.username + ' оказался удачливее')
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Камень", callback_data="button1")
        button2 = telebot.types.InlineKeyboardButton(text="Ножницы", callback_data="button2")
        button3 = telebot.types.InlineKeyboardButton(text="Бумага", callback_data="button3")
        keyboard.row(button1, button2, button3)
        bot.send_message(callback_obj.from_user.id, "Ещё разок?", reply_markup=keyboard)
        bot.send_message(person, "Ещё разок?", reply_markup=keyboard)
        waiting = False
        answer = ''
        person = ''
        name = ''
    elif not waiting:
        waiting = True
        answer = callback_obj.data
        person = callback_obj.from_user.id
        name = callback_obj.from_user.username
    else:
        answer = callback_obj.data
    bot.answer_callback_query(callback_query_id=callback_obj.id)


bot.infinity_polling()
