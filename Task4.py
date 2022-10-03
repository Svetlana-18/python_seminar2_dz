# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

number = int(input("Введите длину списка: "))

list_num = list(range(number))
len_list = len(list_num)
print(list_num)

for i in range(len_list):
    index_rand = random.randint(0, len_list - 1)
    list_num[i], list_num[index_rand] = index_rand, list_num[i]

print(list_num)
