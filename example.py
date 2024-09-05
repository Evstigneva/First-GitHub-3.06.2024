import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

name_one = LinearRegression()
name_one.fit(x, y)
x_name = np.array([[6], [7]])
pred = name_one.predict(x_name)
for i in range(len(x_name)):
    print(f"Предсказанное значение y для x={x_name[i][0]}: {pred[i]}")