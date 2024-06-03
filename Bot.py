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

class APIExeption(Exception):
    pass
class Converter:
    @staticmethod
    def cur_convert(message):
        try:
            text = message.text.lower().split()
            if len(text) > 3:
                raise APIExeption("Введено слишком много аргументов")
            elif len(text) < 3:
                raise APIExeption("Введено слишком мало аргументов")
            else:
                cur_from = text[0]
                cur_to = text[1]
            if cur_from not in currencies.keys() or cur_to not in currencies.keys():
                raise APIExeption(r"Использовано неверное название валюты")
            try:
                amount_from = float(text[2])
            except Exception:
                raise APIExeption('Введена неверная сумма переводимой валюты')

            if text[0] in currencies.keys() and text[1] in currencies.keys():
                cur_from_id = currencies[text[0]]
                cur_to_id = currencies[text[1]]
                amount_from = float(text[2])
                result = requests.get(fr'https://min-api.cryptocompare.com/data/price?fsym={cur_from_id}&tsyms={cur_to_id}') # \request.responce
                result = result.json() # \dict
                result = result[f'{cur_to_id}'] #\float
                amount_to = result * amount_from  # запоминаем сумму в итоговой валюте/ float
                result = f'{amount_from} {cur_from_id}({text[0]}) = {amount_to} {cur_to_id}({text[1]})'  # \string
                bot.send_message(message.chat.id, result)
        except APIExeption as ex:
            bot.send_message(message.chat.id, f'Возникла ошибка: {ex}')
        except Exception:
            bot.send_message(message.chat.id, f'Возникла непредвиденная ошибка. Повторите ввод')


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