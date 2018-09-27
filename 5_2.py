from array import array
import colorama
colorama.init(strip=False)


x = int(input('Введите число элементов массива: '))
count = 0
a = [0 for x in range(x)]

for i in range(0, x):
    a[i] = int(input('Введите {current}/{all} элемент массива: '.format(current = i,all = x)))

for i in range(2,x):
    if (a[i-2] > a[i-1] < a[i]):
        count += 1
    
print('{endcolor}Количество локальных минимумов: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = count, endcolor = colorama.Fore.WHITE))