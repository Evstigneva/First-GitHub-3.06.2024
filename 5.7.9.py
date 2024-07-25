a=int(input())
s=[]
d=0
for i in range(a):
    i=list(input().split())
    s.append(i)
for i in range(a):
    for r in range(a):
        if s[i][r]!=s[r][i]:
            d+=1
if d==0:
    print('Yes')
else:
    print('No')