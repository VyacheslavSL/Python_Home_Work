# Задача 3. Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, 
# который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

list_1 = []
for j in range(5):
    list_1.append(int(input(f'Input number № {j + 1}: ')))
print(f'list_1 = {list_1}')
max_element = max(list_1)

num = abs(int(input('Input number N: ')))
list_2 = []
if num <= max_element:
    for i in range(-num, num + 1):
        list_2.append(i)
    print(f'list_2 = {list_2}')
else:
    print('Error! input number N <= maximum of list_1')

product = 1
for k in range(5):
    product *= list_2[list_1[k]]
print(product)


