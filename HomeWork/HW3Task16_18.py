"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Input: 
5
1 2 3 4 5
3
Output: -> 1
"""
"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Input: 
5
1 2 3 4 5
6
Output: -> 5
"""

import  random

my_list = [random.randint (0,99) for i in range(20)]
print(my_list)
number_x = int(input("Введите число x: "))
count = 0
for i in range(len(my_list)):
    if my_list[i]==number_x:
        count+=1
print(f'число {number_x} встречается {count} раз(а)')
min_dif = abs(number_x- my_list[0])   
min_x_number = my_list[0]    
if count == 0:
    for i in range(1, len(my_list)):
        if abs(number_x-my_list[i]) <=min_dif:
             min_dif= abs(number_x-my_list[i])
             min_x_number = my_list[i]
    print(f'Самый близкий по величине элемент {min_x_number}')