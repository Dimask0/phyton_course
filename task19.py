# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

row = [1, 2, 3, 4, 5]
k = 3
print(row[k:]+row[k:])
