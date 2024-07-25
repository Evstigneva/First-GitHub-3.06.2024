import pandas as pd
a=pd.read_csv('2 intermediate attestation titanic.csv', sep='\t')
for i in a['Age']:
    print(i)
        