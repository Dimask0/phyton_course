# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
#Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
#(необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.


# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

n = int(input())
p =0
k = 1
a =[]
d = []
s1=['a','n','t','o','n']
for i in range(n):
    s = input()
    for j in range(len(s)):
        if j =='a':
            e = 1
            if e==1 and j=='n':
                g = 1
                if e ==1 and g==1 and j =='t':
                    f = 1
                    if e ==1 and g==1 and f ==1 and j=='o':
                        h = 1
                        if e ==1 and g==1 and f ==1 and h ==1 and j =='n':
                            a.append(k)
    k = k + 1
print(*a)