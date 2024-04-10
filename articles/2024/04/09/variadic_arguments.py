

def function(*args, tom, bob):
    print(args, tom, bob)


def otehr_function(tom, bob, *args):
    print(args, tom, bob)

def main() -> None:
    print(f'Hello main from : {__file__}')
    values = [1,2,3,4]
    function(bob="hi bob", tom="hi tom", *values)
    function(bob="hi bob", *values, tom="hi tom")
    function(*values, bob="hi bob", tom="hi tom")
    
    otehr_function("hi bob", "hi tom", *values) # require removal of names
    # otehr_function(bob="hi bob", *values, tom="hi tom")
    # otehr_function(*values, bob="hi bob", tom="hi tom")

if __name__ == '__main__':
    main()
