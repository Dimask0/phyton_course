# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_numbers(a, b):
    if a > b:
        if b == 0:
            return a
    return  sum_numbers(a+1, b-1)
    if a < b:
        if a == 0:
            return b
    return sum_numbers(a-1, b+1)
print(sum_numbers (2,8))