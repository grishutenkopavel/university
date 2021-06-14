
def saveResultInFile(WhatToWrite):
   
    try:
        fileHandler = open('saver.txt', 'a')
        fileHandler.write(WhatToWrite)
    except IOError:
        print('An IOError has occurred!')
    except:
        print("непредвиденная ошибка")
    finally:
        fileHandler.close()

 
def calc():
    strWriteBuff = ''
    isWork = True
    while isWork:
        strCalc = input()
        if (strCalc == ''):
            saveResultInFile(strWriteBuff)
            exit()
        
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
            print("Error")
        try:
            strWriteBuff += strCalc + ' = ' + str(result) + '\n'
        except UnboundLocalError:
            print("ошибка передачи данных")
        print(strCalc + ' = ' + str(result))
    return strWriteBuff


if __name__ == "__main__":
    calc()
    