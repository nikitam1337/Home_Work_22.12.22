# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
import random
N = int(input('Введите длину последовательности чисел: '))
a = int(input('Введите минимальное число в последовательности: '))
b = int(input('Введите максимальное число в последовательности: '))
new_list=[]
for i in range(N+1):
    new_list.append(random.randint(a,b))
print(new_list)

result =[]
for i in new_list:
    if i not in result:
        result.append(i)
print(result)