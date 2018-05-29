from array import array

a = [0 for x in range(10)]
b = [0 for x in range(10)]
c = [0 for x in range(10)]

for i in range(0, 10):
    a[i] = int(input('Введите {}/10 элемент 1 массива: '.format(i)))
for i in range(0, 10):
    b[i] = int(input('Введите {}/10 элемент 2 массива: '.format(i)))

for i in range(0, 10):
    if (i % 2) == 0:
        c[i] = a[i+1]
    else:
        c[i] = b[i-1]

for i in range(0, 10):
    print (c[i])
        
