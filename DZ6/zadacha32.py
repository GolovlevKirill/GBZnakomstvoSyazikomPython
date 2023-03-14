# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

from random import randint
list = []

for i in range(5):
    list.append(randint(-100,100))
    print(list[i])

min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        print(i)
