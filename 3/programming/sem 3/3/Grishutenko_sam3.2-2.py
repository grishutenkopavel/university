"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Шифрование Цезаря
	Скрипт шифрования символов шифром Цезаря на заданную длинну.
	
    Шифрование Цезаря предполагает смещение по таблице на n символов
    в данной программе смещение реализовано с использованием букв
    русского алфавита.
 
"""
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMessage():
    print('Введите текст: ')
    return input()

def getKey():
    print('Введите ключ шифрования: ', end='')
    key = int(input())
    if key > MAX_KEY_SIZE:
        key = key % MAX_KEY_SIZE
    return key

def getTranslatedMessage(message, key):
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= MAX_KEY_SIZE:
                symbolIndex -= MAX_KEY_SIZE

            translated += SYMBOLS[symbolIndex]
    return translated

message = getMessage()
key = getKey()
print(getTranslatedMessage(message, key))  