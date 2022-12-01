# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# number = input('Введите число: ')
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
# number1 = 1
# print(number1, end=' ')
# for i in range(2, num+1):
#     number1 = number1*i
#     print(number1, end=' ')

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

# n = int(input('Введите число: '))
# sum=0
# for i in range(1, n+1):
#     list = (1+1/i)**i
#     print(list, end =' ')
#     sum = sum+list
# print(f'\nСумма чисел равна: {sum}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

# with open('fileforhomework.txt', 'r') as file:
#     place = file.read().split('\n')
# place = list(map(int, place))

# n = int(input('Введите число: '))
# multiplication = 1
# newlist = [i for i in range(-n, n+1)]
# for y in place:
#     multiplication *= newlist[y]
# print(place)
# print(newlist)
# print(multiplication)

# 5. Реализуйте алгоритм перемешивания списка.

# n = int(input('Введите число: '))
# list = [i for i in range(-n, n+1)]
# print(list)
# import random
# random.shuffle(list)
# print(list)