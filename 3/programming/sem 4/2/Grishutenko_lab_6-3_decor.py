import functools

saveInFile = False


def saveResultInFile(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            fileHandler = open('saver.txt', 'a')
            fileHandler.write(func())
        except IOError:
            print('An IOError has occurred!')
        except UnboundLocalError:
            print('непредвиденная ошибка')
        finally:
            fileHandler.close()
    return inner if saveInFile else func


@saveResultInFile
def calc():
    strWriteBuff = ''
    isWork = True
    while isWork:
        strCalc = input()
        if (strCalc == ''):
            break
        listFromUserStr = strCalc.split()
        if (listFromUserStr[1] == '+'):
            result = float(listFromUserStr[0]) + float(listFromUserStr[2])
        elif (listFromUserStr[1] == '-'):
            result = float(listFromUserStr[0]) - float(listFromUserStr[2])
        elif (listFromUserStr[1] == '*'):
            result = float(listFromUserStr[0]) * float(listFromUserStr[2])
        elif (listFromUserStr[1] == '/'):
            result = float(listFromUserStr[0]) / float(listFromUserStr[2])
        else:
            print('Error')

        try:
            strWriteBuff += strCalc + ' = ' + str(result) + '\n'
        except UnboundLocalError:
            print('ошибка передачи данных')
        print(strCalc + ' = ' + str(result))
    return strWriteBuff


if __name__ == '__main__':
    try:
        calc()
    except NameError:
        ('Not callable')
