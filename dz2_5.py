""" Реализуйте алгоритм перемешивания списка. """

from random import random, shuffle

num = int(input('Enter the number of elements: '))
num_list = []
for i in range(num):
    num_list.append(input("Enter the list element: "))
print("Created list: ", num_list)
shuffle(num_list)
print('Mixed list: ', num_list)