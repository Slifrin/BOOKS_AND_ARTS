

def bidirectional_generator():
    print("Initial step of generator")
    counter = 15
    while True:
        print("-" * 50)
        received = yield counter
        counter += 1
        print(f"{received=} {counter=}")


def usage_of_generator():
    gen = bidirectional_generator()
    print("before sending data")
    print(gen.send(None), "sent None")
    print("before sending data")
    print(gen.send(1), "sent 1")
    print("before sending data")
    print(gen.send(2), "sent 2")
    print("before sending data")
    print(gen.send(3), "sent 3")
    print("before sending data")
    print(gen.send(4), "sent 4")


def send_to_generator_with_comments():
    print("\n\n")
    def coro():
        print('before yield')
        a = yield 'the yield value'
        b = yield a
        print('done!')
    c=coro() # this does not execute the generator, only creates it

    # If you use c.send('a value') here it could _not_ do anything with the value
    # so it raises an TypeError! Remember, the generator was not executed yet,
    # only created, it is like the execution is before the `print 'before yield'`

    # This line could be `c.send(None)` too, the `None` needs to be explicit with
    # the first use of `send()` to show that you know it is the first iteration
    print(next(c)) # will print 'before yield' then 'the yield value' that was yield

    print(c.send('first value sent')) # will print 'first value sent'

    # will print 'done!'
    # the string 'the second value sent' is sent but not used and StopIterating will be raised     
    print(c.send('the second value sent'))
    
    print(c.send('oops')) # raises StopIterating



def main() -> None:
    print(f'Hello main from : {__file__}')
    usage_of_generator()
    send_to_generator_with_comments()

if __name__ == '__main__':
    main()