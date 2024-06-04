import requests
from bot_info import bot

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
                amount_from = float(text[2].replace(',', '.'))
            except Exception:
                raise APIExeption('Введена неверная сумма переводимой валюты')
            amount_to = Talking_with_api.get_price(cur_from, cur_to, amount_from)
            result = f'{amount_from} ({text[0]}) = {amount_to} ({text[1]})'  # \string
            bot.send_message(message.chat.id, result)
        except APIExeption as ex:
            bot.send_message(message.chat.id, f'Возникла ошибка: {ex}')
        except Exception:
            bot.send_message(message.chat.id, f'Возникла непредвиденная ошибка. Повторите ввод')

class Talking_with_api:
    @staticmethod
    def get_price(base, quote, amount): # base - валюта из которой переводим, quote - в которую, amount - сумма
# получить итоговую цену, которую впишем в ответ пользователю
        cur_from_id = currencies[base]
        cur_to_id = currencies[quote]
        amount_from = amount
        result = requests.get(
            fr'https://min-api.cryptocompare.com/data/price?fsym={cur_from_id}&tsyms={cur_to_id}')  # \request.responce
        result = result.json()  # \dict
        result = result[f'{cur_to_id}']  # \float
        return result * amount_from  # запоминаем сумму в итоговой валюте/ float

