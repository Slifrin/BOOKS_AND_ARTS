"""
    https://medium.com/@jw_ng/dependency-injection-in-python-c4248a096800
"""

# setting dependencies "services" via constructor

class Client_constructor:
    def __init__(self, foo_service, bar_service):
        if foo_service is None:
            raise ValueError("foo service must be provided")
        if bar_service is None:
            raise ValueError("bar service must be provided")
        self.foo = foo_service
        self.bar = bar_service

    def do_smth(self):
        self.foo.do_stuff()
        self.bar.do_stuff()

# setting dependecies via setter methods

class Client_setters:
    def __init__(self):
        self.foo = None
        self.bar = None
    
    def set_foo_service(self, foo_service):
        if foo_service is None:
            raise ValueError("foo service must be provided")
        self.foo = foo_service
    
    def set_bar_service(self, bar_service):
        if bar_service is None:
            raise ValueError("bar service must be provided")
        self.bar = bar_service

    def validate_dependencies(self):
        if self.foo is None:
            raise ValueError("foo service must be provided")
        if self.bar is None:
            raise ValueError("bar service must be provided")

    def do_stuff(self):
        self.validate_dependencies()

        self.foo.do_smth()
        self.bar.do_smth()

# Method to be invoked

class Clien_calling_method:
    def do_stuff(self, foo_service, bar_service):
        if foo_service is None:
            raise ValueError("foo service must be provided")
        if bar_service is None:
            raise ValueError("bar service must be provided")

        foo_service.do_smth()
        bar_service.do_smth()