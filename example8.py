class DictMixin:
    def to_dict(self):
        dicting={}
        for i in self.__dict__:
            if isinstance(self.__dict__[i], DictMixin):
                dicting[i]=DictMixin.to_dict(self.__dict__[i])
            elif isinstance(self.__dict__[i], list):
                a1=[]
                for r in self.__dict__[i]:
                    a1.append(DictMixin.to_dict(r))
                dicting[i]=a1
            else:
                dicting[i]=self.__dict__[i]
            if isinstance(i, DictMixin):
                DictMixin.to_dict(i)
        return dicting
    def from_list_to_keys(self):
        pass
            
class Phone(DictMixin):
    def __init__(self, number):
        self.number=number
class Person(DictMixin):
    def __init__(self, name, age, addres):
        self.name=name
        self.age=age
        self.address=addres
class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
class Company(DictMixin):
    def __init__(self, name, address):
        self.name=name
        self.address=address

address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}
address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {
    'street': '123 Main St',
    'city': 'Albuquerque',
    'state': 'NM',
    'zip_code': '987654'
}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White'}
walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White',
                            'phone': {'number': '555-1234'}}
company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                         'state': 'NM',
                                         'street': '3828 Piermont Dr',
                                         'zip_code': '12345'},
                             'name': 'SCHOOL'}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': 'Los Pollos Hermanos',
                                        'zip_code': '12345'},
                           'age': 55,
                           'friends': [{'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '123 Main St',
                                                    'zip_code': '987654'},
                                        'age': 30,
                                        'name': 'Walter White',
                                        'phone': {'number': '555-1234'}},
                                         {'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '456 Oak St',
                                                    'zip_code': '12345'},
                                        'age': 27,
                                        'name': 'Jesse Bruce Pinkman',
                                        'phone': {'number': '555-5678'}}],
                            'name': 'Gustavo Fring'}

print('Good')