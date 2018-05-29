import math

w = 0

k = int(input('Введите k: '))
    
for i in range(-2,k):
    a = ((math.pow(-1,i))*(math.factorial(i+3)))/(2*(i+4))
    w = w + a
print("W равно: {0} ".format(w))
