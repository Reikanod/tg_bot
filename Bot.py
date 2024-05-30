import telebot
import lxml.html
from lxml import etree
import requests

tree = etree.parse('Lenta.ru - Новости России и мира сегодня.html', lxml.html.HTMLParser())

main_block = tree.findall('.//*[@id="body"]/div[3]/div[3]/main/div[2]/section[1]/div[1]/div[1]')
for div in main_block:
    for a in div:
        print(a.text.encode('utf-8'))


'''
with open(r'D:\Work\Python\MyData\ReikanodBot_token.txt', 'r') as token:
    bot = telebot.TeleBot(token.read())


@bot.message_handler(content_types=['photo'])
def start(message):
    bot.reply_to(message, "Nice meme XDD")


bot.polling(none_stop=True, interval=0)
'''