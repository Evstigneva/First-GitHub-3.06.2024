class Registration: 
    def __init__(self, login, password):
        self.login=login
        self.password=password
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login):
        a2=0
        if not isinstance(login, str):
            raise TypeError
        a1=0
        if '@' in login:
            if login.count('@')==1:
                a2+=1
        if login.index('@')<login.index('.'):
            a2+=1
        if a2==2:
            self.__login=login
        else:
            raise ValueError
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, a):
        s = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        d=['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
             '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
             'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
             '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']
        a2=0
        if not isinstance(a, str):
            a2+=1
            raise TypeError("Пароль должен быть строкой")
        if len(a)<5 or len(a)>11:
            a2+=1
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not any([i.isdigit() for i in a]):
            a2+=1
        if not any([i.islower() for i in a]) and any([i.isupper() for i in a]):
            a2+=1
        if not all([i in s for i in a]):
            a2+=1
        if not any([i==a for i in d]):
            a2+=1
        if a2==0:
            self.password=a
    @staticmethod
    def is_include_digit(a):
        if not any([i.isdigit() for i in a]):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
    @staticmethod
    def is_include_all_register(a):
        if not any([i.islower() for i in a]) and any([i.isupper() for i in a]):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
    @staticmethod
    def is_include_only_latin(a):
        if not all([i in s for i in a]):
            raise ValueError('Пароль должен содержать только латинский алфавит')
    @staticmethod
    def check_password_dictionary(a):
        d=['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
             '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
             'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
             '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']
        if not any([i==a for i in d]):
            raise ValueError('Ваш пароль содержится в списке самых легких')
try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

#assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')