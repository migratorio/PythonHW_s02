# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = (input('Введите вещественное число: '))
sum = 0
for i in a:
    if i != '.':
        sum += int(i)
print (a, ' -> ',sum)