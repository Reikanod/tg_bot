import telebot
import requests
import os.path
import json

if os.path.exists(r'D:\Work\Python\token_reikanod_bot.txt'):
    with open(r'D:\Work\Python\token_reikanod_bot.txt', 'r') as file:
        TOKEN = file.read()
elif os.path.exists(r'G:\Study\Py projects\token_reikanod_bot.txt'):
    with open(r'G:\Study\Py projects\token_reikanod_bot.txt', 'r') as file:
        TOKEN = file.read()
else:
    print('Файл с токеном не найден')

bot = telebot.TeleBot(TOKEN)

currencies = {
    'рубль' : 'RUB',
    'биткоин' : "BTC",
    "евро" : "EUR",
    "доллар": "USD",
    "фунт" : "GBP",
    "йена" : "JPY",
    "вона" : "KRW"
}

class ConversionExeption(Exception):
    pass
class Converter:
    @staticmethod
    def cur_convert(message):
        try:
            text = message.text.lower().split()
            if text[0] in currencies.keys() and text[1] in currencies.keys():
                cur_from = currencies[text[0]]
                cur_to = currencies[text[1]]
                amount_from = float(text[2])
                result = requests.get(fr'https://min-api.cryptocompare.com/data/price?fsym={cur_from}&tsyms={cur_to}') # \request.responce
                result = result.json() # \dict
                result = result[f'{cur_to}'] #\float
                amount_to = result * amount_from  # запоминаем сумму в итоговой валюте/ float
                result = f'{amount_from} {cur_from}({text[0]}) = {amount_to} {cur_to}({text[1]})'  # \string
                bot.send_message(message.chat.id, result)
            else:
                bot.send_message(message.chat.id,
                                 r"Вы ввели данные в неверном формате. Пожалуйста, ознакомьтесь с правилами бота: используйте команду /help")
        except Exception:
            bot.send_message(message.chat.id,
                             "Возникла неизвестная ошибка, пожалуйста повторите ввод и убедитесь в правильности ввода")

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