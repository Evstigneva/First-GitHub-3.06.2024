a=list(map(int, input().split()))
d={}
d1=[]
a.reverse()
s={a[1]:a[0]}
for i in range(2, len(a)):
    s={a[i]:s}
print(s)