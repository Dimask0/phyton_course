# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 
# 2
import random

from random import randint

n = int(input("Количество монет"))
a = 0
b = 0
monets = [0, 1]
for i in range(n):
    random.shuffle(monets)
    print(f'монеты{monets}')
    if int(monets[0]==0):
        a += 1
    if int(monets[0]==1):
        b += 1
print(f'сумма монет, лежащих на разных сторонах {a, b}')
if a > b:
    ans = a
else:
    ans = b

print(f"минимальное количество монет, которые следует перевернуть{ans}")


