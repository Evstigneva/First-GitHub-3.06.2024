a, s=map(int, input().split())
d=[]
a1=0
s1=0
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(s):
        d1=int(d[i][r])
        a1+=d1
    print(a1, end=' ')
    a1=0
print()
for r in range(s):
    for i in range(a):
        d1=int(d[i][r])
        s1+=d1
    print(s1, end=' ')
    s1=0