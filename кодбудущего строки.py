def fibonacci(a):
    'Возвращает n-ое число Фибоначчи'
    d=[1, 1]
    for i in range(a-2):
        d.append(d[-1]+d[-2])
    if a==0:
        return 0
    else:
        return d[-1]
assert fibonacci(50) == 12586269025
assert fibonacci(60) == 1548008755920
assert fibonacci(70) == 190392490709135
assert fibonacci(80) == 23416728348467685
assert fibonacci(90) == 2880067194370816120
assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
print('Good')