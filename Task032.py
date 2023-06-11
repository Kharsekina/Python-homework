# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


array=[randint(1,101)for i in range(10)]
print(array)
min_num=int(input("Введите минимальное число в диапазоне от 1 до 100: "))
max_num=int(input("Введите максимальное число в промежутке от 1 до 100: "))
for i in range(len(array)):
    if min_num<array[i]<max_num:
        print(i, end=' ')
# print([i for i in range(len(array)) if min_num<array[i]<max_num])
