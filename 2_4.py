import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if  (math.pow(x,2) +  math.pow(y,2)) > (math.pow((x + y),2)):
    print('Сумма квадратов больше')
else:
    print('Квадрат суммы больше')