text = str(input('Enter your text: '))
bad_code = text.split(' ')
bad_code.append('enter')
max_u = 0
u=0
for i in bad_code:
    if i == '':
        u+=1
    else:
        if (u > max_u):
            max_u = u
        u=0

print(max_u)