from random import randint
p = randint(1,20)

print("Введите число: ")
n = float(input("n = "))

mp = 2 * p - 1
while n < mp:
    print(n)
    n += 1
