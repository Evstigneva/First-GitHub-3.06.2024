a=list(input().split(','))
s=[]
d=[]
for i in a:
    i=i.lower()
    if i not in s:
        s.append(i)
        d.append('НЕТ')
    else:
        d.append('ДА')
for i in d:
    print(i)