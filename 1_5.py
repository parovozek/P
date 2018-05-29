import math

x = 3.5
b = 0.4

a = math.log10(x)
c = math.pow(a,2) + math.sqrt(b * x)
y = math.pow(math.e,2 * x) + math.pow(9.7,c)

print(y)
