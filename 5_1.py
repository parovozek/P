from array import array
import colorama
colorama.init(strip=False)

a = [0 for x in range(15)]
count_null = 0
count_otr = 0
proiz = 1
for i in range(0, 15):
    a[i] = int(input('Введите {}/15 элемент массива: '.format(i)))
#Обработаем первый элемент
if (a[0] == 0):
    count_null += 1
elif (a[0] < 0):
        count_otr += 1
#конец обработки
for i in range(1,15):
    if (a[i] > 0):
        temp = a[i-1] * a[i]
        proiz = proiz + temp
    elif (a[i] == 0):
        count_null += 1
    elif (a[i] < 0):
        count_otr += 1
print('{endcolor}Количество отрицательных: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = count_otr, endcolor = colorama.Fore.WHITE))
print('{endcolor}Произведение положительных элементов: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = proiz, endcolor = colorama.Fore.WHITE))
print('{endcolor}Нулевых элементов: {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = count_null, endcolor = colorama.Fore.WHITE))

