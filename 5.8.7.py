a, s=map(int, input().split())
d=[]
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(1, a):
    for r in range(1, s):
        d1=int(d[i][r-1])
        d2=int(d[i-1][r])
        d[i][r]=d1+d2
for i in range(a):
    for r in range(s):
        print(d[i][r], end=' ')
    print()