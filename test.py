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

def round_to_signif(num):
    num_str = str(num)
    a = num_str.find('.')
    num_str = num_str[a + 1:]
    for i in range(len(num_str)):
        if int(num_str[i]):
            return round(num, i + 2)



message = 'доллар рубль 100'

text = message.lower().split()
if text[0] in currencies.keys() and text[1] in currencies.keys():
    cur_from = currencies[text[0]]
    cur_to = currencies[text[1]]
    amount_from = float(text[2])
    result = requests.get(fr'https://min-api.cryptocompare.com/data/price?fsym={cur_from}&tsyms={cur_to}')
    result = result.json()
    result = result[f'{cur_to}']
    amount_to = result * amount_from  # запоминаем сумму в итоговой валюте
    print(type(amount_to), amount_to)
    amount_to = round_to_signif(amount_to)
    print(type(amount_to), amount_to)
    result = f'{amount_from} {cur_from}({text[0]}) = {amount_to} {cur_to}({text[1]})'




    # amount_to = float(result[f'{cur_to}'] * amount_from)  # запоминаем сумму в итоговой валюте
    # amount_to = format(amount_to, '.2g')  # итоговую сумму округляем до двух значимых цифр
    # result = f'{amount_from} {cur_from}({text[0]}) = {amount_to} {cur_to}({text[1]})'
