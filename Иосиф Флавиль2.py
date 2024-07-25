a=int(input())
s=int(input())
d1=int((s*0.35)*2)
d=[]
a1=1
a2=0
for i in range(1, a+1):
    d.append(str(i))
for r in range(int(len(d)**1.35)):
    for i in range(len(d)):
        if 'n' not in d[i] and a1<s and a2<=a-2:
            a1+=1
        elif a1==s and 'n' not in d[i] and a2<=a-2:
            a1=1
            d[i]+='n'
            a2+=1
for i in d:
    if 'n' not in i:
        print(i)