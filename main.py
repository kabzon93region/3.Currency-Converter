import xml.etree.ElementTree as ET
import requests
import datetime as dt
import valdict as vd



dictval = []
vd.get_val_code_dict(dictval)

print("0. (RUB) Российский рубль")
for i in range(len(dictval)):
    print(f"{i+1}. ({dictval[i].iso_code}) {dictval[i].name}")

valcode1: int

while True:
    try:
        valcode1 = int(input("Введите номер валюты первого числа из списка: "))
        if valcode1 > len(dictval) or valcode1 < 0:
            print("!ОШИБКА! : Вы ввели не существующий в списке номер валюты.")
        else:
            break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не число.")


valcode2: int
while True:
    try:
        valcode2 = int(input("Введите номер валюты второго числа из списка: "))
        if valcode2 > len(dictval) or valcode2 < 0:
            print("!ОШИБКА! : Вы ввели не существующий в списке номер валюты.")
        else:
            break
    except ValueError:
        print("!ОШИБКА! : Вы ввели не число.")



now = dt.datetime.now()
date_str = now.strftime("%d.%m.%Y")
if valcode1 == 0:
    cur1 = 1
    cur1 = float(cur1)
    val1 = "RUB"
else:
    #date_str = input(f"Введите дату в формате ДД.ММ.ГГГГ на которую вы хотите узнать курс {dictval[valcode1-1].iso_code}: ")
    cur1 = vd.get_cur_on_date(dictval[valcode1-1].req_code, date_str)
    cur1 = cur1.replace(",", ".")
    cur1 = float(cur1)
    val1 = dictval[valcode1-1].iso_code

if valcode2 == 0:
    cur2 = 1
    cur2 = float(cur2)
    val2 = "RUB"
else:
    #date_str = input(f"Введите дату в формате ДД.ММ.ГГГГ на которую вы хотите узнать курс {dictval[valcode2-1].iso_code}: ")
    cur2 = vd.get_cur_on_date(dictval[valcode2-1].req_code, date_str)
    cur2 = cur2.replace(",", ".")
    cur2 = float(cur2)
    val2 = dictval[valcode2-1].iso_code

num1 = float(input(f"Введите сумму в {val1}, из которого будет проведена конвертация в {val2}: "))

num2 = (num1 * cur1) / cur2

print("Ответ: ", round(num2, 2), val2)


#nameval = [key for key, value in dictval.items() if value == currency_code]
# nameval = str(nameval)
# nameval = nameval.replace("[", "")
#nameval = nameval.replace("'", "")
#nameval = nameval.replace("]", "")

#print(f"Дата: {date}, Название валюты: {nameval}, Код валюты: {currency_code}, Курс: {value}")