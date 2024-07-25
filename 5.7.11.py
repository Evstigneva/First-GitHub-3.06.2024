a, s=map(int, input().split())
d=[]
f=0
a1=0
s1=0
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(s):
        d1=int(d[i][r])
        if d1>f:
            f=d1
            a1=i
            s1=r
print(f)
print(a1, s1)