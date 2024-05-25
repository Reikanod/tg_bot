import telebot

with open(r'D:\Work\Python\MyData\ReikanodBot_token.txt', 'r') as token:
    bot = telebot.TeleBot(token.read())


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, "здарова")
    else:
        bot.send_message(message.from_user.id, 'напиши привет')


bot.polling(none_stop=True, interval=0)
