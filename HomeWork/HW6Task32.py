### Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

# list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list)):
#     if min_number <= list[i] <= max_number:
#         print(i)

import random

n = int(input('Введите количество элементов массива: '))
list_1 = []
for i in range(n):
    list_1.append(random.randint(-10, 10))
print(list_1)
min_number = int(input('Введите минимальный элемент диапазона: '))
max_number = int(input('Введите максимальный элемент диапазона: '))
list_new = []
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_new.append(i)
print(list_new)