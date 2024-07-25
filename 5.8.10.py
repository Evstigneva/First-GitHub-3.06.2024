a, s=map(int, input().split())
d=[]
a1=0
for i in range(a):
    i=input()
    d.append(i)
for i in range(a):
    for r in range(s):
        if d[i][r]=='C' or d[i][r]=='M' or d[i][r]=='Y':
            a1+=1
if a1>0:
    print('#Color')
elif a1==0:
    print('#Black&White')