a=input()
a1=a[-2:]
if a1[0]=='0' or a1[0]!='1':
    a1=a1[1]
a1=int(a1)
if a1==0 or a1>4:
    print(f'{int(a)} рублей')
elif a1==2 or a1==3 or a1==4:
    print(f'{int(a)} рубля')
elif a1==1:
    print(f'{int(a)} рубль')