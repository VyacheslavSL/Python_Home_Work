# Задача 4. Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = abs(int(input('Input number N:')))
sum = 0
for i in range(0 , n + 1, 2):
    sum += i
print(sum)