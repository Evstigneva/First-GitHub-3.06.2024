a=int(input())
s=list(input().split())
d=0
s1=[]
s2=[]
for i in s:
    i=int(i)
    if i>=0:
        s1.append(i)
    elif i<0:
        s2.append(i)
for r in range(len(s1)):
    for r1 in range(len(s1)):
        if s1[r1]>s1[r]:
            s1[r1], s1[r]=s1[r], s1[r1]
            d+=1
for r in range(len(s2)):
    for r1 in range(len(s2)):
        if s2[r1]<s2[r]:
            s2[r1], s2[r]=s2[r], s2[r1]
            d+=1
s2.reverse()
s.clear()
s=s2+s1
print(*s)
print(d)