a, s=map(int, input().split())
d=[]
a1=0
for i in range(a):
    i=input()
    d.append(i)
for i in range(a-1):
    for r in range(s-1):
        d1=d[i][r]
        d2=d[i][r+1]
        d3=d[i+1][r]
        d4=d[i+1][r+1]
        if d1==d2==d3==d4:
            a1+=1
if a1>0:
    print('No')
else:
    print('Yes')
        
