a=int(input())
s=[]
d=0
for i in range(a):
    i=list(input().split())
    s.append(i)
for i in range(a):
    for r in range(a):
        if i==r:
            s1=s[i][r]
            s1=int(s1)
            d+=s1
print(d)