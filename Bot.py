from extentions import *


@bot.message_handler(commands=['start', 'help'])
def start_func(message):
    text = '''Добро пожаловать в обменный бот.
Введите название первой валюты, второй валюты в которую хотите перевести и сумму в формате "доллар рубль 100"
Команды:
/help - помощь
/currencies - список всех доступных для конвертации валют'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['currencies', 'values'])
def show_suppurted_currencies(message):
    text = 'Доступные для конвертации валюты:'
    for key in currencies:
        text += "\n" + key.capitalize() + ": " + currencies[key]
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    Converter.cur_convert(message)



bot.polling()