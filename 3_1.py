import math

print("Введите первое число: ")
a = float(input("a = "))
print("Введите второе число: ")
b = float(input("b = "))

while a > b:
    print("Введите первое число: ")
    a = float(input("a = "))
    print("Введите второе число: ")
    b = float(input("b = "))
c = 0
for  a in range(int(a),int(b)+1):
    print(a)
    c+=1
print("в диапазоне: {0} чисел".format(c))
