class Human:
    @staticmethod 
    def default_name(self):
        pass
    @staticmethod 
    def default_age(self):
        pass
    def __init__(self, name, age, money, house):
        cls.default_name(name)
        cls.default_age(age)
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
    def info(self):
        print(self.name)
        print(self.age)
        print(self.__money)
        print(self.__house)
    @staticmethod
    def default_info(self):
        pass