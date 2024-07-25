a=input()
s=input()
d={}
d1={}
a1=0
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for r in s:
    if r not in d1:
        d1[r]=1
    else:
        d1[r]+=1
if len(d)>len(d1):
    f=d
else:
    f=d1
for i in f:
    if i in d1 and i in d and d[i]==d1[i]:
        a1+=0
    else:
        a1+=1
if a1>0:
    print('NO')
else:
    print('YES')