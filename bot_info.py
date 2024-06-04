import telebot
import os.path

if os.path.exists(r'D:\Work\Python\token_reikanod_bot.txt'):
    with open(r'D:\Work\Python\token_reikanod_bot.txt', 'r') as file:
        TOKEN = file.read()
elif os.path.exists(r'G:\Study\Py projects\token_reikanod_bot.txt'):
    with open(r'G:\Study\Py projects\token_reikanod_bot.txt', 'r') as file:
        TOKEN = file.read()
else:
    print('Файл с токеном не найден')

bot = telebot.TeleBot(TOKEN) # https://t.me/ReikanodBot