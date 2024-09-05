a=list(map(int, input().split()))
s=[]
a1=0
for i in a:
    if i not in s:
        a1+=1
        s.append(i)
print(a1)