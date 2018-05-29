import math

a = True
b = False
c = False 

one = (a or not a and b) or c
two = not a or a and (b or c)
three = (a or b and not c) and c


print('Первое логическое выражение равно: {}'.format(one))
print('Второе логическое выражение равно: {}'.format(two))
print('Третье логическое выражение равно: {}'.format(three))
