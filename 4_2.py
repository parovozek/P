s = input()
 
i = 0
while s[i] == ' ': i+=1
s = s[i:]
 
i = len(s)
while s[i-1] == ' ': i-=1
s = s[:i]
 
s1 = s[0]
i = 1
while i < len(s):
	if s[i] != ' ':
		s1 += s[i]
	elif s[i-1] != ' ':
		s1 += ' '
	i += 1
print(s1+' ')