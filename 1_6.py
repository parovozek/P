import math

t = int(input("Введите число t: "))

s = math.fabs(math.pow(t,3) - 3 * math.pow(t,2) + 2)

print('Скорость тела в момент времени {0} равна {1} '.format(t, s))