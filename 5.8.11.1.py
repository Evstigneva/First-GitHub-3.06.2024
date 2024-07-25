a=int(input())
d=[]
a1=1
a2=0
i=0
r=0
a3=0
for u in range(a):
    u=[0]*a
    d.append(u)
for y in range(a):
    for y1 in range(a):
        if d[y][y1]==0:
            a3=1
for t in range(a):
    for u in range(a):
        if a3==1:
            while r<a-a2:
                if d[i][r]==0:
                    d[i][r]=a1
                    a1+=1
                r+=1
            i+=1
            r-=1
            while i<a-a2:
                if d[i][r]==0:
                    d[i][r]=a1
                    a1+=1
                i+=1
            i-=1
            r-=1
            while r>=a2:
                if d[i][r]==0:
                    d[i][r]=a1
                    a1+=1
                r-=1
            r+=1
            i-=1
            while i>a2:
                if d[i][r]==0:
                    d[i][r]=a1
                    a1+=1
                i-=1
            a3=0
            a2+=1
        for t in range(a):
            for t1 in range(a):
                if d[t][t1]==0:
                    a3=1
        i+=1
        r+=1
for i in range(a):
    for r in range(a):
        print(d[i][r], end=' ')
    print()               