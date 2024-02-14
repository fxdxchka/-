import csv

'''открытие файла
    products - массив, где записаны значения каждый строчки таблицы'''
with open("products.csv", "r", encoding="utf-8-sig", newline="") as f:
    products = list(csv.reader(f, delimiter=";"))[1:]

# print(products)

'''d - новый словарь где будут минимальные значения категорий'''
d = {}
'''заполниение словаря d'''
for i in products:
    x = float(i[-1])
    if i[0] not in d:
        d[i[0]] = i[1], x
    else:
        if x < d[i[0]][1]:
            d[i[0]] = i[1], x

'''вывод значений по введеной категории'''
s = input()
while s != 'Молоко':
    if s in d:
        print(f'В категории: {s} товар: {d[s][0]} был куплен {d[s][1]} раз')
    else:
        print('Такой категории не существует в нашей БД')
    s = input()