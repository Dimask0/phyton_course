# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, 
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284
# 10 минут

list_1 = []
num = 300
number1 = 0
for j in range(num):
    for i in range(1,j):
        if j % i ==0:
            number1 = number1 + i
    list_1.append([j,number1])
    number1 = 0
print(list_1)
for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] ==list_1 [j][0]:
            print(list_1[i])




