a=list(input().split())#1 1 2 2 3 3 4 4 5 5 6 6 
s=[]
s1=[]
a1=a
a=str(a)
a=a.lower()
a=list(a.split())#
for i in range(len(a)):
    if a[i] not in s:
        s.append(a1[i])
print(*s)