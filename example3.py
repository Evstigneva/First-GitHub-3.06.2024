import pandas as pd
import numpy as np
a=pd.read_csv('2 intermediate attestation titanic.csv', sep='\t')
mean=int(a['Age'].mean())
a['Age'].fillna(value=mean, inplace=True)
a1=[]
a2=[]
for i in a.Name:
    i=list(i.split(', '))
    a1.append(i[0])
    a2.append(i[1])
a.Name=a2
a['Surname']=a1
print(a.head())