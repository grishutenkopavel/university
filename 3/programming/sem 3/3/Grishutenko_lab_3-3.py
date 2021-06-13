"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с csv файлом
	Ввод данных в csv файл из json 
	
	Ввод данных в csv файл из json по ключам с помощью импортируемое csv
    библиотеки и использования форматирования строк различными методами
"""
handle = open('data.json')

lines = handle.readlines()


import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for line in lines:
        lst = line.strip('{[]').replace(':', ',').replace('"','').split(',')
        dct = dict(zip(lst[::2],lst[1::2]))
        writer.writerow([dct['id'],dct['first_name'],dct['last_name'],dct['email'],dct['gender'],dct['ip_address'].strip('}')])

handle.close()
