def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }
dd=dict()
while True:
    key = input('введите ключ: ')
    value = input('введите значение: ')

    dd[key] = value
print(flatten_dict(dd))