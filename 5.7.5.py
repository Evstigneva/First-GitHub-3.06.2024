a, s=map(int, input().split())
d=[]
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(s-1, -1, -1):
        print(d[i][r], end=' ')
    print()