a, s=map(int, input().split())
d=[]
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a-1, -1, -1):
    for r in range(s):
        print(d[i][r], end=' ')
    print()