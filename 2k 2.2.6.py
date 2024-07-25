a=int(input())
d=[]
a1=0
for i in range(a):
    i=int(input())
    d.append(i)
f=int(input())
for i in range(a):
    for r in range(i+1, a):
        if d[i]*d[r]==f:
            a1+=1
if a1>0:
    print('ДА')
else:
    print('НЕТ')