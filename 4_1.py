text = "AAAdsdsds" 

d = dict.fromkeys(text, 0) 
for c in text: 
    d[c] += 1 
print (d ['A'])