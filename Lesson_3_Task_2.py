#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#1 2 3 4 5
#6
#-> 5

n = int(input("Введите количество элементов массива: "))
list_1 = []
dif_1 = 100
dif_2 = 100
min_1 = 100
min_2 = 100
result_1 = 0
result_2 = 0
for i in range(n):
    m = int(input("Введите число массива: "))
    list_1.append(m)
x = int(input("Введите число, близкое к которому будем искать: "))
print(n)
print(list_1)
print(x)
for i in range(n):
    if list_1[i] > x:
        dif_1 = list_1[i] - x
        if dif_1 < min_1:
            result_1 = list_1[i]
            min_1 = dif_1
for i in range(n):
    if list_1[i] <= x:
        dif_2 = x - list_1[i]
        if dif_2 < min_2:
            result_2 = list_1[i]
            min_2 = dif_2
if min_1 < min_2:
    print(result_1)
else:
    print(result_2)