a=input()
d=[]
for i in a:
    if i==',' or i=='{' or i=='}' or i==' ':
        a1=0
    else:
        d.append(i)
d=set(d)
print(len(d))