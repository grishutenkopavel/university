"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Возврат списка некоторых значений из входного набора этих значений

    Функция getList для заданного набора значений возвращает список
    из уникальных элементов, содержащихся во входном значении
"""
def getList(*tupleOfValue):
    newlist=[]
    for char in tupleOfValue:
        add = 1
        for element in newlist:
            if element == char:
                add = 0
        if add == 1:
            newlist.append(char)
    return newlist

print(getList(*input().split()))
