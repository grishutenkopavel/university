# Выполнил: Гришутенко_Павел, ИВТ, 2_курс, 2_группа
# задачи для самостоятельного решения по вариантам, которая идет до темы
# функции.
# Вариант: 1

# Задание 1,2
logical_false = 0
logical_true = 1


delimiter = "*"
space_symbol = " "
# стрелка Пирса
header = "* A *" + "* B *" + "* "+" A nor B " + "*"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
# 1 and 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" ***"

res1 = "*   "+str(int(not(bool(logical_true) or bool(logical_true)))) + "   **"
print(inp_str+res1)
# 1 and 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" ***"

res1 = "*   "+str(int(not(bool(logical_true) or bool(logical_false)))) + "   **"
print(inp_str+res1)
# 0 and 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" ***"

res1 = "*   "+str(int(not(bool(logical_false) or bool(logical_true)))) + "   **"
print(inp_str+res1)
# 0 and 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" ***"

res1 = "*   "+str(int(not(bool(logical_false) or bool(logical_false)))) + "   **"
print(inp_str+res1)
print(delimiter * table_width)
print()
# (A∨B)∧ ¬C
header = "* A *" + "* B *" + "* C *"+" (A or B) and not(C) " + "*"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
# (1 or 1) and not 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" ** "+str(logical_true)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_true or bool(logical_true)) and not(bool(logical_true)))))+" "+delimiter*10
print(inp_str+res1)
# (1 or 1) and not 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" ** "+str(logical_false)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_true or bool(logical_true)) and not(bool(logical_false)))))+" "+delimiter*10
print(inp_str+res1)
# (1 or 0) and not 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" ** "+str(logical_true)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_true or bool(logical_false)) and not(bool(logical_true)))))+" "+delimiter*10
print(inp_str+res1)
# (1 or 0) and not 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" ** "+str(logical_false)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_true or bool(logical_false)) and not(bool(logical_false)))))+" "+delimiter*10
print(inp_str+res1)
# (0 or 1) and not 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" ** "+str(logical_true)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_false or bool(logical_true)) and not(bool(logical_true)))))+" "+delimiter*10
print(inp_str+res1)
# (0 or 1) and not 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" ** "+str(logical_true)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_true or bool(logical_false)) and not(bool(logical_true)))))+" "+delimiter*10
print(inp_str+res1)
# (0 or 0) and not 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" ** "+str(logical_true)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_false or bool(logical_false)) and not(bool(logical_true)))))+" "+delimiter*10
print(inp_str+res1)
# (0 or 0) and not 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" ** "+str(logical_false)+" "+delimiter*9

res1 = "* "+str(int((bool(logical_false or bool(logical_false)) and not(bool(logical_false)))))+" "+delimiter*10
print(inp_str+res1)
print(delimiter * table_width)
print()
# ¬B→A∧B∨(¬A→B) = (B or A) and B or (A or B) = (a or b) and (a or b) = a or b
header = "* A *" + "* B *" + "* "+" A or B " + "*"

table_width = len(header)
print(delimiter * table_width)
print(header)
# 1 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) or bool(logical_true)))) + " "+delimiter*6
print(inp_str+res1)
# 1 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_true) or bool(logical_false)))) + " "+delimiter*6
print(inp_str+res1)
# 0 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_false) or bool(logical_true)))) + " "+delimiter*6
print(inp_str+res1)
# 0 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_false) or bool(logical_false)))) + " "+delimiter*6
print(inp_str+res1)
print(delimiter * table_width)
print()

"""
# Комментарий для студента 
# (этот комментарий с 3 по 6 строчку удалить): 
# _________________________
# Для задания 1 и задания2 может быть использована одна доска (борд)
# _________________________

# Описание задачи

  # Постройте таблицу истинности для: 
  # 6. Штрих Шеффера
  
  # или 
  
  # Постройте таблицу истинности для: 
  # 30.	¬(A∧B)∨(C∧B∧A)→¬(A∧¬C↔B∧C)∧¬A∧C∧B∨A
  
  # После этой строчки идет решение задачи, с комментариями (если необходимо)

  30 = 
  
# ___________________________________________________________________

# Задание 3

# Описание задачи

  # Дан список: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
  # Для данного списка, используя слайсы, обращение к элементам по 
  # индексу, методы sum(), min(), max(), арифметические операторы (не используя циклы или условные операторы) найдите:
  
  #19. Список элементов, состоящий из элементов стоящих на нечетных позициях во второй половине списка
  #    и элементов , стоящих на четных позициях первой половины списка. 
  
"""
lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
cntr = int(len(lst)/2)
print(lst[cntr::2]+lst[1:cntr:2])
""" 
  # Дан кортеж: ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight",
   1.230, "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)
  
  # Для данного кортежа, используя слайсы, обращение к элементам по 
  # индексу, методы sum(), min(), max(), арифметические операторы (не используя циклы или условные операторы) найдите:
  
  # 24.	Список, в котором бы содержались размеры автомобиля (длина, ширина, высота).
  """

tp = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230,
      "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)
print(list(tp[11:16:2]))
