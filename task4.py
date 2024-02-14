import csv

'''открытие файла
    products - массив, где записаны значения каждый строчки таблицы'''
with open("products.csv", "r", encoding="utf-8-sig", newline="") as f:
    products = list(csv.reader(f, delimiter=";"))[1:]

'''генерация промокода
    s - массив полученный из списка продукотов'''
def promocode(s):
    x = s[1][0:2] + s[2][0:2] + s[1][-1] + s[1][-2] + s[2][4] + s[2][3]
    return x.upper()
'''Присвоение промокодов в новый столбец'''
for i in products:
    i.append((promocode(i)))

'''Создание нового файла со столбцом promocode'''
with open("products_promo.csv", "w", encoding="utf-8-sig", newline="" ) as f2:
    writer = csv.writer(f2)
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writerows(products)





