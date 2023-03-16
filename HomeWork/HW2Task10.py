# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint
count = int(input("Введите количество монет "))
reverse = 0
for _ in range(count):
    current_coin = randint(0, 1)
    print(current_coin, end=" ")
    if current_coin == 0:
        reverse +=1
print(f'Необходимо перевернуть {reverse if reverse<count/2 else count-reverse} монет(ы)')