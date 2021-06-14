"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Тесты
	Тестирование с использованием assert
	
	Скрипт-файл с тестами для файла Grishutenko_lab_5-1.py
    Тестирование проводится с помощью функции assert
"""
from Grishutenko_lab_5_1 import printTable
from Grishutenko_lab_5_1 import openFile

def test_printTable():

    assert printTable([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}]) != 'dsad : asda'
    assert printTable([{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}]) == "Tony : 123 Dony : rty Bob : [8, 9, 0] "
    assert printTable('[{"Tony":123, "Dony":"rty", "Bob":[8,9,0]}]') == -1


def test_openFile():
    assert openFile('wefwef') == -2
    assert type(openFile('file.json')) == list

if __name__ == "__main__":
    test_printTable()
    test_openFile()
