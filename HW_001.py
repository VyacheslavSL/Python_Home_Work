# Задача № 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите чило соотвтствующее дню недели (От 1 до 7.): ')
num = int(input())

if num == 6 or num == 7:
    print('Этот день выходной')
elif(0 < num < 6):
    print('Этот день рабочий')
else:
    print('Ошибка! Введите число от 1 до 7.')