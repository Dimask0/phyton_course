#Задача No15. 
#Решение в группах 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
#Input: 5 -> 5 1 6 5 9 Output: 1 9

mellons= int(input())
mellons=[5, 1, 6, 5, 9]
min_ =0
max_=0
for mellon in mellons:
    if mellon>max_:
        max_=mellon
    elif mellon<min_:
        min_=mellon
print(max_, min_)