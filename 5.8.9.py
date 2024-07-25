a, s=map(int, input().split())
a2=[]
a1=0
d=[]
d1=[]
for i in range(a):
    for r in range(s):
        a2.append(a1)
        a1+=1
    d.append(a2)
    a2=[]
for i in range(a):
    if i%2==1:
        d[i].reverse()
        d1.append(d[i])
    else:
        d1.append(d[i])
for i in range(a):
    for r in range(s):
        print(d[i][r], end=' ')
    print()