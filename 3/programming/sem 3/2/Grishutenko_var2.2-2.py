"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Возврат списка некоторых значений из входного набора этих значений

    Функция getList для заданного набора значений возвращает список
    из повторяющихся элементов, содержащихся во входном значении
"""
def getList(*tupleOfValue):
    newList = []
    for index in range(len(tupleOfValue)):
        for char in tupleOfValue[index+1:]:
            if tupleOfValue[index] == char:
                exists = 0
                for element in newList:
                    if element == char:
                        exists = 1
                if exists == 0:
                    newList.append(char)
    return newList
        

print(getList(*input().split()))
