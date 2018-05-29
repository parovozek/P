from array import array

a = [0 for x in range(14)]

count_chet = 0
for i in range(0, 14):
    a[i] = int(input('Введите {}/14 элемент массива: '.format(i)))

for i in range(0,14):
    if (a[i] % 2) == 0:
        count_chet += 1
print("Число четных элементов = {}".format(count_chet))
