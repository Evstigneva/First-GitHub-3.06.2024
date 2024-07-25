a=int(input())
d=[]
d1=[]
for i in range(1, a+1):
    d1.append(i)
    d1.append(i**2)
    d.append(d1)
    d1=[]
d=dict(d)
print(d)