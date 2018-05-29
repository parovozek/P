import math

print("Введите число n: ")
n = float(input("n = "))
print("Введите число x: ")
x = float(input("x = "))

summa = 1
i = 0
while n < 1:
    print("Введите число n: ")
    n = float(input("n = "))    
for  i in range(int(i),int(n)):
    a = ((math.pow(x,i)) / (math.factorial(i)))
    summa = summa + a

print("Сумма равна: {0}".format(summa))
