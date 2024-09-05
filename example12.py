import numpy as np
import pandas as pd
d = pd.read_csv('3.4 dataset.csv')
d['Pet+country'] = d['Pet'] + d['Country']
d['Mean_age'] = d['Age'].mean()
from sklearn.cluster import KMeans
age = KMeans(n_clusters=3)
age.fit(d['Age'].to_numpy().reshape(-1,1))
d['clusters'] = pd.Series(age.labels_)