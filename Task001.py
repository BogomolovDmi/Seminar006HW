# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Просмотреть свои предыдущие ДЗ и попробовать применить к ним lambda, filter, map, zip, enumerate, list comprehension, там где это возможно.

# Старое решение:
# n = int(input('Введите число: '))
# def get_squerence(n):
# return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))
# Новое решение:

n = int(input('Введите число: '))
res = list(range(1, n+1))
print(list(map(lambda x: (1+1/x)**x, res)))
print(sum(list(map(lambda x: (1+1/x)**x, res))))