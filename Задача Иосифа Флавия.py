a=int(input())
s=int(input())
d=[]
a1=0
d1=[]
i=0
for i in range(1, a+1):
    d.append(i)
for i in range(a):
    d1.append(i)
for i in d1:
    if a1!=s:
        a1+=1
    elif a1==s and len(d)>1 and i!='':
        f=d1.index(i)
        d1[f]=''
        d.remove(i)
print(d)