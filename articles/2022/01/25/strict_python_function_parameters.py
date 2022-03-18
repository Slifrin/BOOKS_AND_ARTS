'''
    adress : https://sethmlarson.dev/blog/strict-python-function-parameters
    description : passing params to functions
'''


def process_data_1(data, encoding="ascii"):
    print(type(data), id(data), data)
    print(type(encoding), id(encoding), encoding)


def process_data_2(data, *, encoding="ascii"):
    '''
        keywordonly parameters -> introduced in PEP 3102
        The asterisk means that all parameters to the right in the
        function signature can't be passed as positional arguments. 
        These parameters are now "keyword-only".
    '''
    print(type(data), id(data), data)
    print(type(encoding), id(encoding), encoding)


def process_data_3(data, /, encoding="ascii"):
    '''
        positional parameters only -> introduced in PEP 570
        The / in the function signature means that all parameters to the
        left of the / are positional-only. Positional-only parameters
        can't be passed a keyword argument:
    '''
    print(type(data), id(data), data)
    print(type(encoding), id(encoding), encoding)


def process_data_4(data, /, *, encoding="ascii"):
    '''
        strict function signature
    '''
    print(type(data), id(data), data)
    print(type(encoding), id(encoding), encoding)


def main():
    # All positional parameters, tougher to
    # infer the parameter for 'utf-8'.
    process_data_1(b"input", "utf-8")

    # Using `data` as keyword argument, but
    # not as clean as "data" term is duplicated.
    process_data_1(data=b"input")
    process_data_1(data=b"input", encoding="utf-8")

    # All keyword parameters but encoding
    # and data are flip-flopped.
    process_data_1(encoding="utf-8", data=b"input")

    ##############################################################

    # The way you want users to use the function:
    process_data_2(b"input")
    process_data_2(b"input", encoding="utf-8")

    # Raises a TypeError:
    # process_data_2(b"input", "utf-8") # nice

    # What way can (and will) use the function:
    process_data_2(data=b"input")
    process_data_2(data=b"input", encoding="utf-8")
    process_data_2(encoding="utf-8", data=b"input")

    ##############################################################

    # The way you want users to use the function:
    process_data_3(b"input")
    process_data_3(b"input", encoding="utf-8")

    # Raises a TypeError:
    # process_data(b"input", "utf-8") # nice

    ##############################################################

    # The way you want users to use the function:
    process_data_4(b"input")
    process_data_4(b"input", encoding="utf-8")

    # Raises a TypeError:
    # process_data_4(b"input", "utf-8") # nice
    # process_data_4(data=b"input") # nice
    # process_data_4(data=b"input", encoding="utf-8") # nice
    # process_data_4(encoding="utf-8", data=b"input") # nice


if __name__ == '__main__':
    main()