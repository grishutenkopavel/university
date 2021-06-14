"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с исключениями
	Ввод данных из json ввиде таблицы с обработкой исключительных ситуаций
	
	Ввод данных из json парами ключ - значение с использованием
    импортируемого модуля json с применением обработки исключений
"""
try:
    import json
except ImportError:
    print("Ошибка при попытке импартировать модуль")

def openFile(name):
    try:
        with open(name, "r") as read_file:
            try:
                data = json.load(read_file)
            except json.JSONDecodeError:
                print("не json")
        
        return data
    
    except FileNotFoundError:
        print("не найден файл, проверте указанный путь к файлу")
        return -2
    except IOError:
        print("невозможно прочитать/записать. (возможна ошибка прав доступа)")
        return -3
    
    return -1


def printTable(data):
    table = ''
    try:
        for element in data:
            for item in element:
                try:
                    print(item,' : ',element.get(item))
                    table = table + str(item) \
                        + ' : ' + str(element.get(item)) + ' '
                except KeyError:
                    print('Неверное взятие по ключу')
    
        return table
    
    except IndexError:
        print('Неверное итерирование по объекту')
    except:
        return -1

def readAndPrintTable(file_name):
        
    data = openFile(file_name)
    printTable(data)

        

if __name__ == "__main__":
    readAndPrintTable("file.json")

