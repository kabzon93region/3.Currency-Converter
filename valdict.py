import xml.etree.ElementTree as ET
import datetime as dt
import requests

def get_val_code_dict(cur_dict):
    url = 'http://www.cbr.ru/scripts/XML_val.asp'  #http://www.cbr.ru/scripts/XML_val.asp?d=0
    response = requests.get(url)

    # Создание пустого словаря
    currency_dict = {}

    # Парсинг XML-ответа
    root = ET.fromstring(response.content)
    for item in root.iter('Item'):
        # Извлечение данных
        name = item.find('Name').text
        code = item.find('ParentCode').text.strip()  # Удаление пробелов из кода
        # Добавление данных в словарь
        currency_dict[name] = code
    cur_dict.update(currency_dict)


def get_cur_on_date(valcode: str):
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

    while True:
        try:
            date = dt.datetime.strptime(date_str, "%d/%m/%Y")
            date -= dt.timedelta(days=1)
            date_str = date.strftime("%d/%m/%Y")
            date_req: str = date_str

            url = "https://www.cbr.ru/scripts/XML_dynamic.asp"
            params = {"date_req1": date_req, "date_req2": date_req, "VAL_NM_RQ": valcode}

            response = requests.get(url, params=params)

            root = ET.fromstring(response.content)
            value = root.find("Record/Value").text
            return value
            break
        except AttributeError:
            print(f"На дату {date_req} не указан курс ЦБ, проверяем предыдущую дату")