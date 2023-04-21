import xml.etree.ElementTree as ET
import requests
import datetime as dt
import valdict as vd

dictval = {}
vd.get_val_code_dict(dictval)

for i, key in enumerate(dictval.keys()):
    print(f"{i+1}. {key}")

while True:
    try:
        valcode = int(input("Введите номер валюты из списка, курс которой вы хотите узнать: "))
        if valcode > len(dictval.keys()) or valcode < 1:
            print("!ОШИБКА! : Вы ввели не существующий в списке номер валюты.")
        else:
            break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не число.")

value_list = list(dictval.values())

# Запрос даты у пользователя
while True:
    try:
        date_str = input("Введите дату в формате ДД.ММ.ГГГГ на которую вы хотите узнать курс валюты: ")
        date = dt.datetime.strptime(date_str, "%d.%m.%Y")
        date_str = date.strftime("%d/%m/%Y")
        date = dt.datetime.strptime(date_str, "%d/%m/%Y")
        date += dt.timedelta(days=1)
        date_str = date.strftime("%d/%m/%Y")
        break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не дату или не в формате ДД.ММ.ГГГГ.")

date_req: str = ""

while True:
    try:
        date = dt.datetime.strptime(date_str, "%d/%m/%Y")
        date -= dt.timedelta(days=1)
        date_str = date.strftime("%d/%m/%Y")
        date_req: str = date_str

        url = "https://www.cbr.ru/scripts/XML_dynamic.asp"
        params = {"date_req1": date_req, "date_req2": date_req, "VAL_NM_RQ": value_list[valcode-1]}

        response = requests.get(url, params=params)

        root = ET.fromstring(response.content)
        date = root.attrib["DateRange1"]
        currency_code = root.attrib["ID"]
        value = root.find("Record/Value").text
        break
    except AttributeError:
        print(f"На дату {date_req} не указан курс ЦБ, проверяем предыдущую дату")

nameval = [key for key, value in dictval.items() if value == currency_code]
nameval = str(nameval)
nameval = nameval.replace("[", "")
nameval = nameval.replace("'", "")
nameval = nameval.replace("]", "")

print(f"Дата: {date}, Название валюты: {nameval}, Код валюты: {currency_code}, Курс: {value}")