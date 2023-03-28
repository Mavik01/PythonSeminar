'''
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы
массива. Массив состоит из целых чисел.
Ввод: 
5 
1 2 3 4 5
Вывод:
0
Ввод:
5
1 5 1 5 1
Вывод:
2
'''

# import random

# n = int(input('Введите количество элементов массива: '))

# arr = []
# for i in range(n):
#     arr.append(random.randint(1, 10))

# print(arr)

# count = 0
# for i in range(n):
#     if arr[i-2] < arr[i-1] > arr[i]:   # такая нумерация не позволит выйти за пределы массива
#         count += 1

# print(count)
# интересный вариант строки 31 с условием
#     if arr[i-1] < arr [i] > arr [(i + 1) % len(arr)]: 
# % когда i достигнет предела массива, деление с остатком на само себя даст 0 
#  и превратиться в аrr[0]



# сокращенная запись этого кода

# from random import randint

# list = [randint(1, 20) for i in range(int(input('Введите количество элементов массива: ')))]

# print(list)

# count = 0
# for i in range(len(list)):
#     if list[i-2] < list[i-1] > list[i]:   # такая нумерация не позволит выйти за пределы массива
#         count += 1

# print(count)

import random

list_1 = [random.randint(1, 20) for _ in range(int(input('Введите размер списка: ')))]

print(list_1)

count = 0
for i in range(1, len(list_1)-1):
    
    if list_1[i-1] < list_1[i] > list_1[i+1]:
        count += 1
print(count)