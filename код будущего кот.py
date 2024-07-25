a=input()
a1=''
a2=0
for i in a:
    if len(a1)==0 and (i=='к' or i=='К'):
        a1+=i
    elif len(a1)==1 and (i=='о' or i=='О'):
        a1+=i
    elif len(a1)==2 and (i=='Т' or i=='т'):
        a1+=i
    elif len(a1)==3:
        a2+=1
print(a2)