import textwrap

import faker


fake = faker.Faker()


def alter_some_text():
    text = fake.paragraph(nb_sentences=10)
    print(text)

    for line in textwrap.wrap(text):
        print(line)

    print(textwrap.fill(text))


def remowing_whitspaces():
    s = """
    hello 
        there
    """
    print(repr(s))
    print(repr(textwrap.dedent(s)))


def add_whitespaces():
    s = 'hello\n\n \nworld'
    print(textwrap.indent(s, "    "))
    print(textwrap.indent(s, "+ ", lambda line: True))


def main() -> None:
    print(f'Hello main from : {__file__}')
    alter_some_text()
    remowing_whitspaces()
    add_whitespaces()

if __name__ == '__main__':
    main()
