"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	
    ResolveLogicFunction() - выписывает таблицу с решенным логическим выражением
                             с различными значениями переменных
    getHeader() - возвращает строку заголовка
    showTable() - отображает границы ascii таблицы

    в лябда-функциях описаны логические выражения которые необходимо решить,
    чтобы показать таблицу; в logicFunctionN хранится список с переменными и
    лоничеким выражением
"""
ResolveLogicFunction1 = lambda a, b: not(a or b)
ResolveLogicFunction2 = lambda a, b, c: (a or b) and not c
ResolveLogicFunction3 = lambda a, b: a or b
def getHeader(logicFunction):
    header = '**'
    for element in logicFunction:
        header += element+'**'
    return header
    
def ResolveLogicFunction(logicFunction, tableLen, ResolveLogicFunctionX):
    countVariables = len(logicFunction)
    lenLogicFuntion = len(logicFunction[countVariables-1])
    variations = 2**(countVariables-1)
    for i in range(variations):
        stringBin = str(bin(i))[2:]
        while len(stringBin) != countVariables:        
            stringBin = '0'+stringBin    
        listBoolValues = list(stringBin[1:])
        logicstr = ''
        for element in listBoolValues:
            logicstr += '**' + element
        boolLogicList = [bool(int(element)) for element in listBoolValues]
        logicstr += '**'+'*'*int(lenLogicFuntion/2 + 1)+str(int(ResolveLogicFunctionX(*boolLogicList)))
        logicstr += '*'*(tableLen - len(logicstr))
        print(logicstr)
        
def showTabel(header, logicFunction, ResolveLogicFunctionX):
    delimetr = '*'
    tableLen = len(header)
    print(delimetr*tableLen)
    print(header)
    print(delimetr*tableLen)
    ResolveLogicFunction(logicFunction, tableLen, ResolveLogicFunctionX)       
    print(delimetr*tableLen)
    print()
logicFunction1 = ['a', 'b', 'not (a or b)']
logicFunction2 = ['a', 'b', 'c', '(a or b) and not c']
logicFunction3 = ['a', 'b', 'a or b']
header1 = getHeader(logicFunction1)
header2 = getHeader(logicFunction2)
header3 = getHeader(logicFunction3)
showTabel(header1, logicFunction1, ResolveLogicFunction1)
showTabel(header2, logicFunction2, ResolveLogicFunction2)
showTabel(header3, logicFunction3, ResolveLogicFunction3)
