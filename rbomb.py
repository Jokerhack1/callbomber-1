import requests, time, json, random
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
WHITE = colorama.Fore.WHITE

print('Автор скрипта не несет ответственности. Использовать на свой страх и риск.')
CHOOSE = input("Согласен? (y/n) > ")
if CHOOSE == 'y':
	pass
elif CHOOSE == 'n':
	exit()
else:
	print("Введено неправильное значение.")
	exit()

while True:
	phone = input("Введи номер телефона (без +) >> ")
	if phone.startswith("+"):
		print("Введите номер БЕЗ +")
	elif phone.startswith("7") and len(phone) == 11:
		print(phone[1:4])
		print(phone[4:7])
		print(phone[7:9])
		print(phone[9:11])
		break
	else:
		print("Некорректный номер!")

while True:
	name = input("Введите имя лица, от которого будут посылаться запросы >> ")
	if name == "":
		print("Некорректное имя!")
	else:
		break

with open("services.json", "r") as read_file:
	services = json.load(read_file)

for dicts in services:
	for keys in dicts["data"]:
		dicts["data"][keys] = dicts["data"][keys].replace("%phone1%", phone[1:4])
		dicts["data"][keys] = dicts["data"][keys].replace("%phone2%", phone[4:7])
		dicts["data"][keys] = dicts["data"][keys].replace("%phone3%", phone[7:9])
		dicts["data"][keys] = dicts["data"][keys].replace("%phone4%", phone[9:11])
		dicts["data"][keys] = dicts["data"][keys].replace("%name%", name)

with open("user_agents.json", "r") as read_file:
	user_agents = json.load(read_file)

print("\nЧтобы остановить скрипт нажми CTRL+C или CTRL+Z.")
while True:
	session = requests.session()
	for item in services:
		r = session.post(item["url"], headers = {"X-Requested-With": "XMLHttpRequest",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": user_agents[random.randint(0, 140)],}, json = item["data"])

		if r.status_code == 200:
			print("{}[{}] запрос на звонок отправлен!{}".format(GREEN, item["name"], WHITE))
		else:
			print("{}[{}] запрос не отправлен, код: {}{}".format(RED, item["name"], str(r.status_code), WHITE))
	
	time.sleep(5)















































































