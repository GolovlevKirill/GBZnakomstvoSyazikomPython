# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх 
# решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

print ('Введите общее число монет:')
n = int(input())

print('Введите 0 если монетка лежит вверх гербом.')
print('Введите любую другую цифру если монетка лежит вверх решкой')
count_gerb = 0
count_reshka = 0

for i in range(n):
    x = int(input())
    if x == 0:
        count_gerb += 1
    else:
        count_reshka += 1

print('Нужно перевернуть:')
if count_gerb == count_reshka:
    print(count_gerb)

if count_gerb > count_reshka:
    print(count_reshka)

if count_reshka > count_gerb:
    print(count_gerb)
