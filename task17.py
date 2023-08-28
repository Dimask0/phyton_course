# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(lst)
lst1 =[]
for i in lst:
    if i not in lst1:
        lst.append(i)
print(lst1)
print(len(lst1))
