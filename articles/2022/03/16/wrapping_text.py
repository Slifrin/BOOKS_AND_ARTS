"""
    https://docs.python.org/3/library/textwrap.html
"""

import textwrap



def main():
    print(f'Hello main from : {__file__}')
    a = "a" * 250
    print(textwrap.wrap(a))
    print(textwrap.fill(a))
    print(textwrap.shorten(a, width=40))
    
    s = """\
        hello
          world
    """
    print(s)
    print(textwrap.dedent(s))


if __name__ == '__main__':
    main()