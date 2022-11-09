"""
    https://developer.ibm.com/tutorials/os-pythondescriptors/
"""
from pprint import pprint

# Creating descriptors using class method

class Descriptor:

    def __init__(self):
        self._name = ''
    
    def __get__(self, instance, owner):
        print(f'Getting: {self._name}')
        return self._name

    def __set__(self, instancem, value):
        print(f'Setting: {value}')
        self._name = value

    def __delete__(self, instance):
        print(f'Deleting: {self._name}')
        del self._name

class PersonV1:
    name = Descriptor()

def descriptor_class_implementation():
    user = PersonV1()
    user.name = 'Tom'
    print(user.name)
    del user.name

class PersonV2:
    def __init__(self):
        self._name = ''

    def fget(self):
        print(f'Getting: {self._name}')
        return self._name

    def fset(self, value):
        print(f'Setting: {value}')
        self._name = value

    def fdel(self):
        print(f'Deleting: {self._name}')
        del self._name

    name = property(fget, fset, fdel, 'I\'m the property')

def descripto_propery_type():
    user = PersonV2()
    user.name = 'Tom'
    print(user.name)
    del user.name

class PersonV3:
    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print(f'Getting: {self._name}')
        return self._name

    @name.setter
    def name(self, value):
        print(f'Setting: {value}')
        self._name = value

    @name.deleter
    def name(self):
        print(f'Deleting: {self._name}')
        del self._name

def descripto_propery_decorator():
    user = PersonV3()
    user.name = 'Tom'
    print(user.name)
    del user.name

class PersonWithDynamicProperty:
    def addProperty(self, attribute):
        getter = lambda self: self._get_roperty(attribute)
        setter = lambda self, value: self._set_property(attribute, value)

        setattr(self.__class__, attribute, property(getter, setter, doc='Auto-generated method'))

    def _set_property(self, attribute, value):
        print(f'Setting: {attribute}')
        setattr(self, 'MY_attr_' + attribute, value) # it is required as public attribute set in addProperty alread has that name :)

    def _get_roperty(self, attribute):
        print(f'Getting: {attribute}')
        return getattr(self, 'MY_attr_' + attribute)

def check_dynamic_property():
    person = PersonWithDynamicProperty()
    pprint(dir(person))
    person.addProperty('name')
    person.name = 'Tom'
    person.addProperty('age')
    person.age = 42
    pprint(dir(person))
    pprint(person)


def main() -> None:
    print(f'Hello main from : {__file__}')
    # descriptor_class_implementation()
    # descripto_propery_type()
    # descripto_propery_decorator()
    check_dynamic_property()


if __name__ == '__main__':
    main()