# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

mnoj = [int(x) for x in input().split()]
n = mnoj[0]
m = mnoj[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
merges = set_1 & set_2
result = list(merges)
result.sort()
for i in result:
    print(i, end=' ')

# array1 = set(map(int, input().split()))
# array2 = set(map(int, input().split()))
# s_set = sorted(array1.intersection(array2))
# print(*s_set)