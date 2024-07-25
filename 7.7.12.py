def print_goods(*args):
    s=1
    d=[]
    for i in args:
        if type(i)==str and len(i)>0:
            d.append(f'{s}. {i}')
            s+=1
    if len(d)==0:
        print('Нет товаров')
    else:
        for i in d:
            print(i)
#a=input()
print_goods(1, True, 'Грушечка', '', 'Pineapple')
