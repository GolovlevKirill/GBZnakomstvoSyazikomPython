# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input('Введите колличество эллементов 1-го множества'))
m = int(input('Введите колличество эллементов 2-го множества'))
set1 = {}
set2 = {}

set1 = set(set1)
set2 = set(set2)


for i in range(0,n,1):
    set1.add(int(input("Введите эллементы 1-го множества(в множестве не может быть одинаковых эллементов):")))

for i in range(0,m,1):
    set2.add(int(input("Введите эллементы 2-го множества(в множестве не может быть одинаковых эллементов):")))


print('Первое множество:', set1)
print('Второе множество:', set2)

print('Общие числа:', set1 & set2)


