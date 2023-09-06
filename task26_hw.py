#Задача 26:Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8

def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))
A = int(input("Введите число: "))
B = int(input("Введите его степень: "))
print( 'A =',A, 'B =',B, "->", power(A, B))

# def Pow(a,b):
#     if b == 0:
#         retutn 1
#     return Pow(a,b-1)*a