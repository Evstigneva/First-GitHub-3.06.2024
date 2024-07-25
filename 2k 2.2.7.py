a=input()
s=input()
a1='камень'
a2='ножницы'
a3='бумага'
if a==s:
    print('ничья')
elif a==a1 and s==a2:
    print('Тимур')
elif a==a2 and s==a1:
    print('Руслан')
elif a==a2 and s==a3:
    print('Тимур')
elif a==a3 and s==a2:
    print('Руслан')
elif a==a1 and s==a3:
    print('Руслан')
elif a==a3 and s==a1:
    print('Тимур')
    