import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

c = ((math.fabs(a)+math.fabs(b))/2)
d = (math.sqrt(math.fabs(a)*math.fabs(b)))

print('Полусумма равна: {}'.format(c))
print('Квадраьный корень произведения модуля: {}'.format(d))