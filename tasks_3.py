#Задание №3

#Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

a = int(input('Введите целое число "А": ')) # 2
b = int(input('Введите целое число "B": ')) # 8
print('Диапазон вех чётных чисел A - B: ')
for i in range(a, b):
    if i % 2 == 0:
     print(i, end = (' '))
    

