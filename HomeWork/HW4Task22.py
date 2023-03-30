# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.



import random

def create_list(size: int) -> list:
    return [random.randint(0,30) for _ in range(size)]

list_1 = create_list(20)
list_2 = create_list(10)

print(list_1)
print(list_2)

list_1 = set(list_1)
list_2 = set(list_2)

final = sorted(list_1.intersection(list_2))

print(final)