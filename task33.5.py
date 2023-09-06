# найти факториал числа N с помощью рекурсии
n = 6
def factorial(x):
    if x == 1:
       return 1
    return x * factorial(x - 1)
  
print(factorial(n))