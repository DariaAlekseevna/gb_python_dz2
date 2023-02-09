""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""


list = []
list_pos = []
k = 0
multi = 1

N = int(input('Enter a number(N): '))

for i in range(-N, N + 1):
    list.append(i)
print(f'List from -N to N: {list}')

#я не понимаю что за файл txt, поэтому пусть позиции вводит пользователь

num_pos = int(input('Enter number of positions: '))
for j in range(1, num_pos + 1):
    list_pos.append(int(input('Enter the position: ')))
print(f'Index list: {list_pos}')

while k < len(list_pos):
    multi *= list[list_pos[k]]
    k += 1
print(f'Product of elements at the entered positions = {multi}')