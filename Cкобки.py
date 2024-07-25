a=input()
s=0
s1=0
s2=0
s3=0
n=0
m=2
c=1
if a[0]==']' or a[0]=='}' or a[0]==')':
    print('NO')
    exit()
for i in a:
    if i=='(':
        s1+=1
    elif i==')':
        if s1>0:
            s1-=1
        else:
            print('NO')
            exit()
    elif i=='[':
        s2+=1
    elif i==']':
        if s2>0:
            s2-=1
        else:
            print('NO')
            exit()
    elif i=='{':
        s3+=1
    elif i=='}':
        if s3>0:
            s3-=1
        else:
            print('NO')
            exit()
while len(a)>=2:
    a1=a[0:2]
    if a1=='(]':
        print('NO')
        exit()
    elif a1=='(}':
        print('NO')
        exit()
    elif a1=='[)':
        print('NO')
        exit()
    elif a1=='[}':
        print('NO')
        exit()
    elif a1=='{)':
        print('NO')
        exit()
    elif a1=='{]':
        print('NO')
        exit()
    else:
        a=a[c:]
        c+=1
if s1==0 and s2==0 and s3==0:
    print('YES')
else:
    print('NO')