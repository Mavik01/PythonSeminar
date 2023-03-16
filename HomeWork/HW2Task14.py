"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
не превосходящие числа N.
10 -> 0 1 2 3
"""

number = int(input('Введите число '))
numsquare = 1
degree = -1
while numsquare <= number:
    numsquare *= 2
    degree += 1
    print(degree, end=' ')