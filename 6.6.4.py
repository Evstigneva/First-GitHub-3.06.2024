a=int(input())
d=[]
s={}
d1=[]
q=''
w=''
for i in range(a):
    i=input()
    d.append(i)
for i in d:
    if i not in s:
        s[i]=0
        d1.append(i+'0')
    else:
        s[i]+=1
        d1.append(i+str(s[i]))
for i in d1:
    if i[-1]=='0':
        print('OK')
    else:
        print(i)