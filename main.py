import xml.etree.ElementTree as ET
import requests
import datetime as dt
import valdict as vd

dictval = {}
vd.get_val_code_dict(dictval)

for i, key in enumerate(dictval.keys()):
    print(f"{i+1}. {key}")
valcode1: int
while True:
    try:
        valcode1 = int(input("Введите номер валюты первого числа из списка: "))
        if valcode1 > len(dictval.keys()) or valcode1 < 1:
            print("!ОШИБКА! : Вы ввели не существующий в списке номер валюты.")
        else:
            break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не число.")


valcode2: int
while True:
    try:
        valcode2 = int(input("Введите номер валюты второго числа из списка: "))
        if valcode2 > len(dictval.keys()) or valcode2 < 1:
            print("!ОШИБКА! : Вы ввели не существующий в списке номер валюты.")
        else:
            break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не число.")

value_list = list(dictval.values())

# Запрос даты у пользователя



print(vd.get_cur_on_date(value_list[valcode1 - 1]))


#nameval = [key for key, value in dictval.items() if value == currency_code]
# nameval = str(nameval)
# nameval = nameval.replace("[", "")
#nameval = nameval.replace("'", "")
#nameval = nameval.replace("]", "")

#print(f"Дата: {date}, Название валюты: {nameval}, Код валюты: {currency_code}, Курс: {value}")