"""
	Автор: Гришутенко Павел, группа№1, подгруппа№2
	Программа выводит последовательно симфолы латинского икириллического
    алфавита с использованием кодов из таблицы unicode-символов.
 
"""
aEngCode = 65
zEngCode = 90
aEngSCode = 97
zEngSCode = 122
aRusCode = 1040
yaRusCod = 1103

for code in range(aEngCode, zEngCode+1):
    print(chr(code), end='')
for code in range(aEngSCode, zEngSCode+1):
    print(chr(code), end='')
print()
for code in range(aRusCode, yaRusCod+1):
    print(chr(code), end='')