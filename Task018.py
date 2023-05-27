# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
# -> 5

size=int(input("Введите размер массива: "))
import random
array = [random.randint(0, 11) for i in range(size)]
print(array)
number=int(input("Введите число от 1 до 10:"))
first=abs(array[0]-number)
result=array[0]
for i in array:
    if abs(i-number)<first:
        result,first=i,i-number 
    i+=1    
print(f"Ближайший к {number} по величине элемент равен {result}")
