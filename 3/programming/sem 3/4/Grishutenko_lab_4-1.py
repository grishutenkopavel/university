"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с json файлом
	Ввод данных из json ввиде таблицы 
	
	Ввод данных из json парами ключ - значение с использованием
    импортируемого модуля json с применением обработки исключений
"""
try:
    import json
except ImportError:
    print("Ошибка при попытке импартировать модуль")

try:
    with open("data.json", "r") as read_file:
        try:
            data = json.load(read_file)
        except json.JSONDecodeError:
            print("не json")
        
        try:
            for element in data:
                for item in element:
                    try:
                        print(item,' : ',element.get(item))
                    except KeyError:
                        print('Неверное взятие по ключу')

        except IndexError:
            print('Неверное итерирование по объекту')

except FileNotFoundError:
    print("не найден файл")
except IOError:
    print("невозможно прочитать/записать. (возможна ошибка прав доступа)")

