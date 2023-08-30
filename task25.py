# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
input_string = 'aaabcaadcdd'
middle = {}
output = []
for i in input_string:
    if i in middle:
        output.append(f"{i}_{middle[i]}")
    else:
        output.append(i)
    middle[i] = middle.get(i,0)+1
result = (output)
print(result)

