import math

y = int(input("Введите число y: "))
f = int(input("Введите число f: "))

g = (math.exp(2 * y) + math.sin(f)) / (math.log10(3.8 * y + f))

print(g)