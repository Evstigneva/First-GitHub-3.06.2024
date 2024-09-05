a=list(map(int, input().split()))
a1=len(a)
for i in range(1, a1, 2):
    a[i], a[i-1]=a[i-1], a[i]
print(*a)