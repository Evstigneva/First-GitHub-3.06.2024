a=list(input().split())
s=[]
d=[]
a1=a
a=str(a)
a=a.lower()
a=list(a.split())
a2=a[::-1]
for u in range(len(a)):
    s.append(u)
for i in a:
    a3=a.count(i)
    if a3>1:
        a4=a3
        a5=0
        while a3>1:
            if a5==0:
                s1=a.index(i)
                print(s1)
                s.remove(s1)
                a2.remove(i)
            else:
                s1=a.index(i)
                s1=s1-a5
                s.remove(s1)
                a2=remove(i)
            a3-=1
            a5+=1
for t in  s:
    d.append(a1[t])
print(*d)