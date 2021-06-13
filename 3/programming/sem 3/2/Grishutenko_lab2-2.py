"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	
    Пользоватьле вписывает в лямбда функцию парметры и выражение логического выражения,
    также в сипосок logicFunction1 сначала вносятся имена переменных, а затем логическое
    выражение, например, ['a','b', 'not a and b']
"""
# в лямбда-функцию вписываются переменные и логическое выражение
ResolveLogicFunction1 = lambda a, b, c: not((a or b) and not c)

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

# в список вписываются переменные и логическое выражение
logicFunction1 = ['a', 'b','c', 'not((a or b) and not c)']
header1 = getHeader(logicFunction1)
showTabel(header1, logicFunction1, ResolveLogicFunction1)

