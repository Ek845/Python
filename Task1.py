# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a=int(input("Введите трехзначное число: "))
print(int(a/100)+int(a%100/10)+int(a%10))