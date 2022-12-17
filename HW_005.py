# Задача № 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Введите координаты точки А')
x_A, y_A = float(input()), float(input())
print('Введите координаты точки B')
x_B, y_B = float(input()), float(input())

from math import sqrt

distance = sqrt((x_B - x_A)**2 + (y_B - y_A)**2) 
print(round(distance, 3))