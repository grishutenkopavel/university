''' Автор: Гришутенко Павел
    
    Создание программы по распределению списка с случайными значениями
    на два списка по определенному критерию (четность/нечетность,
    положительные/отрицательные числа) '''

import random


getRandomList = lambda n: [random.randint(-100, 100) for _ in range(n)]

lst = getRandomList(20)
lst1 = []
lst2 = []

def sortEvenness(mainList, lst1, lst2):
    
    for i in mainList:
        if i % 2 == 0:
            lst1.append(i)
        else:
            lst2.append(i)


def sortSign(mainList, lst1, lst2):

    for i in mainList:
        if i >= 0:
            lst1.append(i)
        else:
            lst2.append(i)


sortEvenness(lst, lst1, lst2)
print(lst1)
print(lst2)
lst1.clear()
lst2.clear()

sortSign(lst, lst1, lst2)
print(lst1)
print(lst2)