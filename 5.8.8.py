a, s=map(int, input().split())
d=[]
d1=[]
f=[]
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a-1, -1, -1):
    for r in range(s-1, -1, -1):
        d1.append(d[i][r])
    f.append(d1)
    d1=[]
print(*f)
for i in range(1, a):
    for r in range(1, s):
        d2=int(f[i][r-1])
        d3=int(f[i-1][r])
        f[i][r]=d2+d3
for i in range(a-1, -1, -1):
    for r in range(s-1, -1, -1):
        print(f[i][r], end=' ')
    print()