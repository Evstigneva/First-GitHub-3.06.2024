from string import ascii_lowercase
d=[]
d1=[]
for i in range(26):
    d1.append(ascii_lowercase[i])
    d1.append(i+1)
    d.append(d1)
    d1=[]
d=dict(d)
print(d)