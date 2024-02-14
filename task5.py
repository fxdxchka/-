import csv

'''открытие файла
    products - массив, где записаны значения каждый строчки таблицы'''
with open("products.csv", "r", encoding="utf-8-sig", newline="") as f:
    products = list(csv.reader(f, delimiter=";"))[1:]
'''cоздание хеш таблицы с помощью словаря
d - новый словарь
'''
d={}
for i in products:
    x = float(i[-1])
    if i[0] not in d:
        d[i[0]] = x
    else:
       d[i[0]] += x

'''сортировка значений словаря'''
a = list(d.values())
a.sort()
'''вывод наименьших 10 продоваемых продуктов'''
for i in range (10):
    for j in d:
        if d[j] == a[i]:
            print(f'{j}, {a[i]}')


