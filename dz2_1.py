""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11 """

# я сначала подумала так, но потом решила и без continue, поэтому решила оставить два решения
""" sum = 0
number = input("Enter number: ")
for i in range(len(number)):
    if (number[i] == ".") or (number[i] == ",") or and (number[i] == "-"):
        continue
    else:
        sum += int(number[i])
print(sum) """

sum = 0
number = input("Enter number: ")
for i in range(len(number)):
    if (number[i] != ".") and (number[i] != ",") and (number[i] != "-"):
        sum += int(number[i])
print(f'The sum of the digits in a number = {sum}')
