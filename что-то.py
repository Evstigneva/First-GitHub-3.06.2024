import pandas as pd
a=pd.read_csv('countries.csv', sep=',')
s=a.sort_values('countries')
age={}
for i in s.loc():
    if i['countries'] not in age and isinstance(a['age'], (int, float)):
        age[i['countries']]=[]
        age[i['countries']].append(i['age'])
    elif i['countries'] in age and  not isinstance(a['age'], (int, float)):
        age[i['countries']].append(0)
    elif i['countries'] not in age and not isinstance(a['age'], (int, float)):
        age[i['countries']]=[]
        age[i['countries']].append(0)  
    else:
       age[i['countries']].append(i['age'])
for i in age:
    print(len(age[i]), sum(age[i])/len(age[i]))