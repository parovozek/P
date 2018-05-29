import math

x = int(input("Введите число байт x: "))

a = x / math.pow(2,10)
b = x / math.pow(2,20)
c = x / math.pow(2,30)
d = x / math.pow(2,40)

print('{0} байт - {1} килобайт'.format(x, a))
print('{0} байт - {1} магабайт'.format(x, b))
print('{0} байт - {1} гигабайт'.format(x, c))
print('{0} байт - {1} терабайт'.format(x, d))