import math

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if (((a % 2 == 0) and (b % 2 != 0)) or ((a % 2 != 0) and (b % 2 == 0))):
    one = True
else:
    one = False 

if (((a % 3) and (b % 3) and (c % 3)) == 0):
    two = True
else: 
    two = False

print('Первое условие равно: {}'.format(one))
print('Второе условие равно: {}'.format(two))