# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n=int(input("Введите номер билета (6 цифр): "))
a=int(n/100000)+int(n/10000%10)+int(n/1000%10)
print(int(a))
b=int(n/100%10)+int(n/10%10)+int(n%10)
print(int(b))
if a==b:
    print("yes")
elif a!=b:
    print("no")
