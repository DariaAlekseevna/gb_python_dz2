""" Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму. """

n = int(input('Enter a number (n): '))
sum = 0
print('[ ', end='')
for i in range(1, n + 1):
    sum += (1 + 1/i)**i
    if i != n:
        print(f'For {i} is {round(sum, 2)};', end='  ')
    else:
        print(f'Finally for {i} is {round(sum, 2)}', end=' ')
print(']')