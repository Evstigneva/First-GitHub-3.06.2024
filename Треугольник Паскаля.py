a=int(input())
s=[]
for i in range(a+1):
    s.append([1]+[0]*a)
for i in range(1, a+1):
    for r in range(1, i+1):
        s[i][r]=s[i-1][r]+s[i-1][r-1]
for i in range(a+1):
    for r in range(i+1):
        print(s[i][r], end=' ')
    print()