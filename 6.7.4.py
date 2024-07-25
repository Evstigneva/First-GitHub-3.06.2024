a=input()
d={}
for i in a:
    i=i.lower()
    if i.isalpha() and i not in d:
        d[i]=1
    elif i.isalpha():
        d[i]+=1
print(d)