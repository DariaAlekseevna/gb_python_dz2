""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

product_if_num = 1
N = int(input("Enter a number(N): "))
print('Product of numbers from 1 to N = [', end=' ')
for i in range(1, N + 1):
    product_if_num *= i
    #print(f'Product of numbers = {product_if_num}')
    print(f'{product_if_num}', end='')
    if i != N:
        print(', ', end='')
    else:
        print(' ', end='')
print(']')