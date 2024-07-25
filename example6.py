class User:
    def __init__(self, name, balance=0):
        self.login=name
        self.balance=balance
    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, a):
        self.__balance=a
    def deposit(self, a):
        self.__balance+=a
    def is_money_enough(self, a):
        return a<=self.__balance
    def payment(self, a):
        if self.__balance>=a:
            self.__balance-=a
        else:
            print('Не хватает средств на балансе. Пополните счет')
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
class Cart:
    def __init__(self, user):
        self.user=user
        Cart.goods={}
        self.__total=0
    def add(self, product, count=1):
        if product.name in Cart.goods:
            Cart.goods[product.name]+=count
        else:
            Cart.goods[product.name]=count
        self.__total+=product.price*count
    def remove(self, product, count):
        if self.__total>=product.price*count:
            self.total-=product.price*count
        if Cart.goods[product.name]>=count:
            Cart.goods[product.name]-=count
    @property
    def total(self):
        return self.__total
    def order(self):
        if Cart.payment(self.__total)=='Не хватает средств на балансе. Пополните счет':
            print('Проблема с оплатой')
        else:
            print('Заказ оплачен')
    def print_check(self):
        print('---Your check---')
        a=sorted(Cart.goods)
        s=Product()
        for i in a:
            print(i, s.price, a[i], s.price*a[i])
        print(f'---Total: {self.__total}---')
billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20

