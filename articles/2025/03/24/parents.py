class GrandParent:
    def greet(self):
        print("Hello from GrandParent")

class Parent(GrandParent):
    def greet(self):
        print("Hello from Parent")
        # This would normally call GrandParent.greet() if using super()
        # super().greet()

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        # Skip Parent.greet() and call the next method in MRO after Parent,
        # which is GrandParent.greet() in this case.
        super(Parent, self).greet()

if __name__ == "__main__":
    child = Child()
    child.greet()