a=int(input())
d=[]
a1=0
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(a):
        if i+r==a-1:
            d1=int(d[i][r])
            if d1>a1:
                a1=d1
print(a1)