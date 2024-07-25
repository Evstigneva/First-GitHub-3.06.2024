a, s=map(int, input().split())
d=[]
if a<=s:
    d=[i*i for i in range(a, s+1)]
elif s<a:
    d=[i**3 for i in range(a, s-1, -1)]
print(d)