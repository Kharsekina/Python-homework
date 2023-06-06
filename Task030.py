# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

array_size=int(input("Введите длинну массива: "))
first_num=int(input("Введите первое число: "))
step=int(input("Введите разность арифметической прогрессии: "))
sequence=[]
for i in range(array_size):
    sequence.append(first_num+step*i)
print(sequence)
# print([sequence.append(first_num+step*i)for i in range(array_size)])