import pandas as pd
a=pd.read_csv('2.5 donut.csv')
a=a.plot(x='x', y='y')
print(a)
