a=int(input())
d=[]
a1=0
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(0, a):
    for r in range(2):
        d1=d[i][r]
        if r==1:
            r1=0
        elif r==0:
            r1=1
        for i1 in range(i+1, a):
           d2=d[i1][r1]
           if d1==d2:
               a1+=1
print(a1)