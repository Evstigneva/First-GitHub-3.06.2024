a=int(input())
s1=0
if a==1:
    print('0')
elif a!=1:
    for i in range(a+1, a*2):
        s=0
        for r in range(1, i+1):
            if i%r==0:
                s+=1
        if s==2:
            s1+=1
    print(s1)