a=list(map(int, input().split()))
a1=0
for i in range(1, len(a)):
    if a[i]>a[i-1]:
        a1+=1
print(a1)