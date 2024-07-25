a=int(input())
s=[]
for i in range(a):
    i=list(input().split())
    s.append(i)
for r in range(a-1, 0-1, -1):
    for i in range(a-1, 0-1, -1):
        print(s[i][r], end=' ')
    print()