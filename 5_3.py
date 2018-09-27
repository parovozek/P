import colorama
colorama.init(strip=False)

char_list = []
x = str(input('Введите число в 10 системе: '))

y = ''
x = bin(x)
x>>y
for i in x:
    char_list.append(i)

char_list.insert(0,0)

y = ''.join(char_list)

f = int(x) + int(y)

print('{endcolor}В сумме сложение чисел (ответ в 10 СС): {color}{out}{endcolor}'.format(color = colorama.Fore.GREEN, out = f, endcolor = colorama.Fore.WHITE))



