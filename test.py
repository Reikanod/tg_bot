import json
import requests

currencies = {
    'рубль' : 'RUB',
    'биткоин' : "BTC",
    "евро" : "EUR",
    "доллар": "USD",
    "фунт" : "GBP",
    "йена" : "JPY",
    "вона" : "KRW"
}





message = 'рубль доллар 100'

text = message.lower().split()
if text[0] in currencies.keys() and text[1] in currencies.keys():
    cur_from = currencies[text[0]]
    cur_to = currencies[text[1]]
    amount_from = float(text[2])
    result = requests.get(fr'https://min-api.cryptocompare.com/data/price?fsym={cur_from}&tsyms={cur_to}')
    result = result.json()

    result = result[f'{cur_to}']
    print(type(result))

    amount_to = result * amount_from  # запоминаем сумму в итоговой валюте/ float
    result = f'{amount_from} {cur_from}({text[0]}) = {amount_to} {cur_to}({text[1]})' # \string
