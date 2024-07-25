import pandas as pd
a=pd.read_csv('2.4 sales.csv', sep=',')
s=pd.read_csv('2.4 weather.csv', sep=',')
a['temperature']=s['temperature']
print(a)