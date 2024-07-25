a, s=map(int, input().split())
d=[]
d1=[]
d2=[]
a1=0
a2=0
for i in range(a):
    i=list(input())
    d.append(i)
for i in range(a):
    for r in range(s):
        if d[i][r]=='S':
            d[i][r]='1'
        else:
            d[i][r]='0'
for i in range(a):
    if '1' in d[i]:
        a1+=1
    else:
        a1=0
    if a1==0:
        d[i].clear()
        a2+=s
        a-=1
    else:
        d1.append(d[i])
d=[]
for i in range(s):
    for r in range(a):
        d.append(d1[r][i])
    d2.append(d)
    d=[]
for i in range(s):
    if '1' in d2[i]:
        a1+=1
    else:
        a1=0
    if a1==0:
        a2+=a
print(a2)