a=int(input())
sv, sn, sgd=map(int, input().split())
d=[]
for i in range(a):
    i=[0]*a
    d.append(i)
for i in range(a):
    for r in range(a):
        if i>r:
            d[i][r]=sn
        elif i==r:
            d[i][r]=sgd
        elif i<r:
            d[i][r]=sv
for i in range(a):
    print(*d[i])