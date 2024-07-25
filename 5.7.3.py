a=int(input())
s=[]
for i in range(a):
    i=list(input().split())
    s.append(i)
for r in range(a):
    for i in range(a):
        print(s[i][r], end=' ')
    print()