"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с json файлом
	Ввод данных из json ввиде таблицы и тестирование программы 
	
	Ввод данных из json парами ключ - значение с использованием
    импортируемого модуля json с применением модуля unittest
"""
try:
    import json
    import unittest
except ImportError:
    print("Ошибка при попытке импартировать модуль")

#простая реализация unit тестирования для программы
class TestDataHandlerMethods(unittest.TestCase):

    def test_dataEqual(self):
        self.assertFalse([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}] == "Tony : 123 Dony : rty Bob : [8, 9, 0] ")
        self.assertTrue([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}] != "Tony : 123 Dony : rty Bob : 8 9 0 ")


def dataPrint(data):

    strdata = ""
    try:
            for element in data:
                for item in element:
                    try:
                        print(item,' : ',element.get(item))
                        strdata += str(item) +' : '+ str(element.get(item)) + " "
                    except KeyError:
                        print('Неверное взятие по ключу')

    except IndexError:
            print('Неверное итерирование по объекту')
    
    return strdata


def main():
    try:
        with open("data.json", "r") as read_file:
            try:
                data = json.load(read_file)
            except json.JSONDecodeError:
                print("не json")

            #dataPrint(data) #если нужен вывод json
    except FileNotFoundError:
        print("не найден файл")
    except IOError:
        print("невозможно прочитать/записать. (возможна ошибка прав доступа)")


main()

if __name__ == '__main__':
    unittest.main()


