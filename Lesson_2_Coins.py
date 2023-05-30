# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть


n = int(input("Введите количество монет: "))
count_0 = 0
count_1 = 0
for i in range(n):
    k = input("Какой стороной лежит монета? Орел - 0; решка - 1: ")
    if k == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_0 > count_1:
    print("Количество монет, которые нужно перевернуть: ", count_1)
else:
    print("Количество монет, которые нужно перевернуть: ", count_0)
