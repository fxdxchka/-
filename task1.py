import csv
'''открытие файла
    products - массив, где записаны значения каждый строчки таблицы'''
with open("products.csv", "r", encoding="utf-8-sig", newline="" ) as f:
    products=list(csv.reader(f, delimiter=";"))[1:]
# print(products)
'''s_z - argument, sum of products from category Zakuski'''
s_z = 0
'''Цикл - добавление в каждую строку будующей таблицы значение столбца тотал'''
for i in products:
    i.append(float(i[-2])*float(i[-1]))

'''Пересчет суммы значение продуктов из Закусок'''
for i in products:
    if i[0]=='Закуски':
        s_z += i[-1]

print(s_z)
'''Создание нового файла со столбцом тотал'''
with open("products_new.csv", "w", encoding="utf-8-sig", newline="" ) as f2:
    writer = csv.writer(f2)
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writerows(products)


