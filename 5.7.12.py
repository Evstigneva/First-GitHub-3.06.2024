a, s=map(int, input().split())
d=[]
d2=[]
max1=0
max2=0
sumax=0
summ=0
a1=0
a2=[]
a3=[]
a4=[]
for i in range(a):
    i=list(input().split())
    d.append(i)
for i in range(a):
    for r in range(s):
        d1=int(d[i][r])
        summ+=d1
    d2.append(summ)
    summ=0
for i in range(a):
    for r in range(s):
        d1=int(d[i][r])
        if d1>max1:
            max1=d1
            a2.clear()
            a2.append(max1)
            a1=i
            a3.clear()
            a3.append(i)
        elif d1==max1:
            a2.append(max1)#максималка список  
            a3.append(i)#индексы строк с максималкой
if len(a2)>1:
    for i in a3:
        for r in range(s):
            d1=int(d[i][r])
            sumax+=d1
        a4.append(sumax)#суммы на строках с максималкой
        sumax=0
    for i in a4:
        i=int(i)
        if i>max2:
            max2=i#максимальная сумма
    q=d2.index(max2)
    print(q)
elif len(a2)==1:
    print(a3[0])
     