"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с json файлом
	Ввод данных из json ввиде таблицы и тестирование программы
	
	Ввод данных из json парами ключ - значение с использованием
    импортируемого модуля json с применением модуля doctest
"""
try:
    import json
except ImportError:
    print("Ошибка при попытке импартировать модуль")


def dataPrint(data):
    '''
    Testing

    >>> dataPrint([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}])
    Tony  :  123
    Dony  :  rty
    Bob  :  [8, 9, 0]
    '''

    try:
            for element in data:
                for item in element:
                    try:
                        print(item,' : ',element.get(item))
                    except KeyError:
                        print('Неверное взятие по ключу')

    except IndexError:
            print('Неверное итерирование по объекту')

try:
    with open("data.json", "r") as read_file:
        try:
            data = json.load(read_file)
        except json.JSONDecodeError:
            print("не json")

        dataPrint(data)

except FileNotFoundError:
    print("не найден файл")
except IOError:
    print("невозможно прочитать/записать. (возможна ошибка прав доступа)")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

