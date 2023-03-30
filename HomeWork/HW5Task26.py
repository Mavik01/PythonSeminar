# Задача 26
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# def ab(i, k):
#     if k == 1:
#         return i
#     else:
#         return i * ab(i, k - 1)
a = int(input("Введите число А: "))
b = int(input("Введите степень В: "))
def func(number, degree):
    return 1 if degree == 0 else number * func(number, degree - 1)
print(func(a,b))
