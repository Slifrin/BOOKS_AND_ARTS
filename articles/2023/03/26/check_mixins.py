"""
A mixin is a class that provides method implementations for reuse by multiple
related child classes. However, the inheritance is not implying an is-a relationship.
A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.
A mixin bundles a set of methods for reuse. Each mixin should have a single
specific behavior, implementing closely related methods.
"""
import json

from pprint import pprint


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


def check_new_employee():
    e = Employee(
        name="John",
        skills=["Ironing", "Running"],
        dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']},
    )
    print(e)

class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)
        return result
    
    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BetterEmployee(DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


def check_new_employee_with_improvments():
    e = BetterEmployee(
        name="John",
        skills=["Ironing", "Running"],
        dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']},
    )
    pprint(e.to_dict())


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict()) # it is only ment to be used as mixin


class BetterBetterEmployee(DictMixin, JSONMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


def check_new_employee_with_more_improvments():
    e = BetterBetterEmployee(
        name="John",
        skills=["Ironing", "Running"],
        dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']},
    )
    pprint(e.to_json())
    print(BetterBetterEmployee.__mro__)

def main() -> None:
    print(f'Hello main from : {__file__}')
    check_new_employee()
    check_new_employee_with_improvments()
    check_new_employee_with_more_improvments()

if __name__ == '__main__':
    main()