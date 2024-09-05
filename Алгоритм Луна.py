a=list(input())
a1=0
for i, r in enumerate(a):
    i=int(i)
    r=int(r)
    if i%2==1:
        a1+=r
    elif i%2==0:
        r*=2
        if r>9:
            r-=9
            a1+=r
        else:
            a1+=r
print(a1%10==0)