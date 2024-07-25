a=int(input())
s=[]
a1=0
for i in range(a):
    i=list(input().split())
    s.append(i)
for i in range(a-1):
    for r in range(2):
        d1=s[i][r]
        if r==1:
            r1=0
        elif r==0:
            r1=1
        for t in range(1, a):
            d2=s[t][r1]
            if d1==d2:
                a1+=1
print(a1)