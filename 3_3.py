import math

print("Введите число: ")
a = float(input("a = "))
print("Введите степень в которую хотите возвести число: ")
n = float(input("n = "))

b = math.pow(a,n)

print("Число {0} в степени {1} равно {2} ".format(a,n,b))