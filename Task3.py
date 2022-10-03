# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

position_one = int(input('Введите первую позицию элемента: ')) - 1
position_two = int(input('Введите вторую позицию элемента: ')) - 1
number = int(input('Введите число N: '))
list_numbers = []
for i in range(-number, number + 1):
    list_numbers.append(i)
print(f'{list_numbers}')
len_list = len(list_numbers)
if position_one > len_list or position_two > len_list or \
        position_one < 0 or position_two < 0 or number <= 0:
    print('Некорректные данные, повторите ввод согласно условию задачи')
else:
    result = list_numbers[position_one] * list_numbers[position_two]
    print(result)
