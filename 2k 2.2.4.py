a=list(map(int, input().split()))
a1=[0]*len(a)
a1[0]=a[-1]
for i in range(1, len(a)):
    a1[i]=a[i-1]
print(*a1)