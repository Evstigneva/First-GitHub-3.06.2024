a=[]
d=0
for i in range(5):
    i=list(input().split())
    a.append(i)
for i in range(5):
    for r in range(5):
        if a[i][r]=='1':
            s=i+1
            s1=r+1
if s>=3:
    d=d+s-3
else:
    d=d+3-s
if s1>=3:
    d=d+s1-3
else:
    d=d+3-s1
print(d)