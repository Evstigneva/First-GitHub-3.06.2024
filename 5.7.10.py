a, s=map(int, input().split())
d=[]
f=[]
a1=0
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(s):
        d1=int(d[i][r])
        a1+=d1
    f.append(a1)
    a1=0
g=max(f)
g1=f.index(g)
print(g)
print(g1)