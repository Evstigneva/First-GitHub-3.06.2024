a, s=map(int, input().split())
q=0
d=[]
d1=[]
a1=a+2
s1=s+2
f='.'*s1
d1.append(f)
for i in range(a):
    i=input()
    d.append(i)
for i in range(a):
    i='.'+d[i]+'.'
    d1.append(i)
d1.append(f)
for i in range(1, a+1):
    for r in range(1, s+1):
        d2=d1[i-1][r]
        d3=d1[i][r-1]
        d4=d1[i][r+1]
        d5=d1[i+1][r]
        d6=d1[i][r]
        if d2==d3==d4==d5==d6=='.':
            q+=1
print(q)
        
    