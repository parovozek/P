import math

x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
c = int(input("Введите число c: "))

l = (math.sqrt(math.exp(x)- math.pow(math.cos(math.pow(x,2) * math.pow(a,5)),4))) / (math.e * math.sqrt(math.fabs(a + x * math.pow(c,4))))

print(l)