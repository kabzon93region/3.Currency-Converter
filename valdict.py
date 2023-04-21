import xml.etree.ElementTree as ET
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

# Вывод словаря на экран
#print(currency_dict)

