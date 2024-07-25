a, s=map(int, input().split())
d=[]
d1=[]
d2=[]
a1=0
a2=[]
a3=''
for i in range(a):
    i=input()
    d.append(i)
e=input()
for i in range(a):
    i=input()
    d1.append(i)
for i in range(a):
    for r in range(s):
        if d[i][r]=='W':
            #a2.append('B')
            a3+='B'
        elif d[i][r]=='B':
            #a2.append('W')
            a3+='W'
    d2.append(a3)
    #a2=[]
    a3=''
for i in range(a):
    for r in range(s):
        f=d1[i][r]#у васи
        f1=d2[i][r]#у меня
        if f==f1:
            a1+=0
        else:
            a1+=1
print(a1)