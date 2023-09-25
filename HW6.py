import random

""" 30. Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
прогрессии: an = a1 + (n-1) * d.Каждое число вводится с новой строки. """

first_elemet = int(input('Введите первый элемент: '))
diff = int(input("Введите разность: "))
length = int(input("Введите длинну массива: "))
list_1 = [first_elemet * i * diff for i in range(length)]
print(list_1)

""" .32 Определить индексы элементов массива (списка), значения которых принадлежат заданному 
 диапазону (т.е. не меньше заданного минимума и не больше заданного максимума) """
 
num_min = int(input("Введите минимальное значение для диапазона: "))
num_max = int(input("Введите максимальное значение для диапазона: "))
lenght_array = int(input("Введите длинну массива: "))
list_1 = [random.randint(-24, 24) for i in range(lenght_array)]
list_2 = []
for i in range(lenght_array):
    if list_1[i] >= num_min and list_1[i] <= num_max:
        list_2.append(i)
print(list_2)
""" list_2 = [i for i in range(lenght_array) if list_1[i] >= num_min and list_1[i] <= num_max ] """
