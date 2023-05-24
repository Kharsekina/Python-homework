# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 0-решка, 1-герб

coin_count=int(input("Введите кол-во монет: "))
zero_count=0
one_count=0
for i in range(coin_count):
    x=int(input("Введите 0 если монета лежит решкой вверх и 1 если монета лежит вверх гербом: "))
    if x==0:
        zero_count+=1
    else:
        one_count+=1
if zero_count<one_count:
    print(zero_count)
else:
    print(one_count)