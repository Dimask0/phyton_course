# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

n = 5

def is_prime(n, dil=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % dil == 0:
        return False
    if dil * dil> n:
        return True
    return is_prime(n, dil + 1)