a=int(input())
a1=0
a2=0
a3=0
a4=0
for i in range(a):
    i=list(map(int, input().split()))
    if i[0]>0 and i[-1]>0:
        a1+=1
    elif i[0]<0 and i[-1]>0:
        a2+=1
    elif i[0]<0 and i[-1]<0:
        a3+=1
    elif i[0]>0 and i[-1]<0:
        a4+=1
print(f'Первая четверть: {a1}')
print(f'Вторая четверть: {a2}')
print(f'Третья четверть: {a3}')
print(f'Четвертая четверть: {a4}')