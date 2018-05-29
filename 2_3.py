import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if ((y < -x + 1) and (x <= 1) and (x >= -1) and (y <= 1) and (y >= -1)) or ((y < x + 1) and (x <= 1) and (x >= -1) and (y <= 1) and (y >= -1)) or ((y < -x - 1) and (x <= 1) and (x >= -1) and (y <= 1) and (y >= -1)) or ((y < x - 1) and (x <= 1) and (x >= -1) and (y <= 1) and (y >= -1)):
    print('Точка принадлежит графику')
else:
    print('Точка не принадлежит графику')