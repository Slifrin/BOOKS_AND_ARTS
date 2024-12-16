
"""
generators create values
corutines consume them 

So it is best not to mix those two
"""

def simple_grep(pattern_to_find):
    print(f"Lokking for pattern {pattern_to_find}")
    counter = 0
    while True:
        line = yield counter
        counter += 1
        if pattern_to_find in line:
            print(line)

def corutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@corutine
def simple_grep_with_helper(pattern_to_find):
    print(f"Lokking for pattern {pattern_to_find}")
    counter = 0
    try:
        while True:
            line = yield counter
            counter += 1
            if pattern_to_find in line:
                print(line)
    except GeneratorExit:
        print("Closing generator")

def main() -> None:
    print(f'Hello main from : {__file__}')
    grep = simple_grep("python")
    next(grep)
    print(grep.send('Hello there'))
    print(grep.send('Hello again'))
    print(grep.send("Hello python"))

    grep_2 = simple_grep_with_helper("python")

    print(grep_2.send('Hello there'))
    print(grep_2.send('Hello again'))
    print(grep_2.send("Hello python"))
    grep_2.close()

if __name__ == '__main__':
    main()