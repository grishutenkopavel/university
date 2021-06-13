"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Работа с json файлом
	Ввод данных из json ввиде таблицы и тестирование программы 
	
	Ввод данных из json парами ключ - значение с использованием
    импортируемого модуля json с применением модуля pytest
"""
try:
    import json
    import pytest
except ImportError:
    print("Ошибка при попытке импартировать модуль")

def test_t1():
    assert dataPrint([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}]) == \
        "Tony : 123 Dony : rty Bob : [8, 9, 0] "
    assert dataPrint([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}]) != \
        "Tony : 123 Dony : rty Bob : 8 9 0 "


def test_t2(el): 
    #в функцию должен передаваться словарь
    with pytest.raises(KeyError):
        el.get("TEST_FILD") #намеренно заваленный тест,попытка получить 
                            #значение по несуществующему ключу


def dataPrint(data):

    strdata = ""
    try:
            for element in data:
                for item in element:
                    try:
                        print(item,' : ',element.get(item))
                        strdata += str(item) + ' : ' + \
                            str(element.get(item)) + " "
                        
                    except KeyError:
                        print('Неверное взятие по ключу')

    except IndexError:
            print('Неверное итерирование по объекту')
    
    return strdata


try:
    with open("data.json", "r") as read_file:
        try:
            data = json.load(read_file)
        except json.JSONDecodeError:
            print("не json")

        dataPrint(data) #если нужен вывод json
except FileNotFoundError:
    print("не найден файл")
except IOError:
    print("невозможно прочитать/записать. (возможна ошибка прав доступа)")