import xml.etree.ElementTree as ET
import datetime as dt
import requests


class cbrval:
    name: str = None
    req_code: str = None
    iso_code: str = None

    def __init__(self, name, req_code, iso_code):
        self.name = name
        self.req_code = req_code
        self.iso_code = iso_code

def gts():
    glist = []
    for i in range(50):
        glist.append(cbrval("name-"+str(i), "req_code-"+str(i), "iso_code-"+str(i)))
    print(glist.name)

def get_val_code_dict(cur_dict: list):
    url = 'http://www.cbr.ru/scripts/XML_valFull.asp'  #http://www.cbr.ru/scripts/XML_val.asp?d=0
    response = requests.get(url)
    root = ET.fromstring(response.content)
    for item in root.iter('Item'):
        name = item.find('Name').text
        req_code = item.find('ParentCode').text
        iso_code = item.find('ISO_Char_Code').text
        cur_dict.append(cbrval(name, req_code, iso_code))


def get_cur_on_date(valcode: str, date_str: str):
    while True:
        try:
            date = dt.datetime.strptime(date_str, "%d.%m.%Y")
            date_str = date.strftime("%d/%m/%Y")
            date = dt.datetime.strptime(date_str, "%d/%m/%Y")
            date += dt.timedelta(days=1)
            date_str = date.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("!ОШИБКА! : Вы ввели не дату или не в формате ДД.ММ.ГГГГ.")
            date_str = input("Введите дату в формате ДД.ММ.ГГГГ на которую вы хотите узнать курс валюты: ")

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