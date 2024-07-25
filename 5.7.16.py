a, s=map(int, input().split())
d=[]
d1=[]
a1=0
for i in range(a):
    i+=1
    for r in range(a):
      r+=1
      d2=i*r
      d1.append(d2)
    d.append(d1)
    d1=[]
for i in range(a):
    for r in range(a):
        d1=int(d[i][r])
        if d1==s:
            a1+=1
print(a1)