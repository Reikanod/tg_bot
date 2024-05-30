import redis

red = redis.Redis(host='127.0.0.1', port=6379)

print('''get Имя - получить номер
set Имя, номер(без пробелов) - внести номер
del Имя - удалить номер
stop - остановить программу''')

while True:
    text = input("Введите команду: ")
    text = text.strip()
    text = text.lower()
    text = text.split()
    match text[0]:
        case "get":
            print(red.get(text[1]))
            continue
        case "set":
            red.set(text[1], text[2])
            continue
        case 'del':
            red.delete(text[0])
        case 'stop':
            break
        case _:
            print("неверно введена команда")
            continue
