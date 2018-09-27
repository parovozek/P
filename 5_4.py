from random import random
import colorama
colorama.init(strip=False)

M = 10
N = 10
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print('{color}   | {sum}{endcolor}'.format(color = colorama.Fore.RED,sum = sum(b), endcolor = colorama.Fore.WHITE))
print()
#print('{color}   | {sum}{endcolor}'.format(color = colorama.Fore.RED,sum = sum(b), endcolor = colorama.Fore.WHITE))