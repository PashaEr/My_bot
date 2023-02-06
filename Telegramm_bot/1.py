
import telebot

bot = telebot.TeleBot('6148650234:AAFzu9kbhCexgfOjjTmYU0TgLBgDgyXvy64')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name} !'
    bot.send_message(message.chat.id, mess)
    photo = open('боты0.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    mess_1 = f'Меня зовут ТЕЛЕБОТИК , хочешь узнать что я умею?'
    bot.send_message(message.chat.id, mess_1)

@bot.message_handler(content_types=['text'])
def get_user_text2(message):
    if message.text == 'да':
        bot.send_message(message.chat.id, f'Отлично,с удовольствием покажу: \n'
                                          f'Я могу рассказать актуальный гороскоп на 2023 год,'
                                          f'\nДля этого нажми эту кнопку "/goroskop" ')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, f'Отлично,с удовольствием покажу: \n'
                                          f'Я могу рассказать актуальный гороскоп на 2023 год !'
                                          '\nДля этого нажми эту кнопку "/goroskop" ')
    elif message.text == 'нет':
        bot.send_message(message.chat.id, f'Ну нет, так нет, {message.from_user.first_name} (')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, f'Ну нет, так нет, {message.from_user.first_name} (')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, f'И тебе привет, {message.from_user.first_name} !')
    elif message.text == 'Привет':
        bot.send_message(message.chat.id, f'И тебе привет, {message.from_user.first_name} !')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')
    elif message.text == '/goroskop':
        bot.send_message(message.chat.id, f'Введите знак зодиака с большой буквы')
    elif message.text == 'Овен':
        photo = open('Овен.png','rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Близнецы':
        photo = open('Близнецы.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Весы':
        photo = open('Весы.png','rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Водолей':
        photo = open('Водолей.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Дева':
        photo = open('Девы.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Козерог':
        photo = open('Козероги.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Лев':
        photo = open('Лев.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Рак':
        photo = open('Рак.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Рыбы':
        photo = open('Рыбы.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Скорпион':
        photo = open('Скорпион.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Стрелец':
        photo = open('Стрелец.png', 'rb')
        bot.send_document(message.chat.id, photo)
    elif message.text == 'Телец':
        photo = open('Телец.png', 'rb')
        bot.send_document(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f'Некорректный ввод')






bot.polling(none_stop = True)

