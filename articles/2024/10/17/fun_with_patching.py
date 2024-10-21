
from io import StringIO
from unittest.mock import patch, NonCallableMock




thing = object()
print(thing)

with patch('__main__.thing', new_callable=NonCallableMock) as mock_thing:
    assert thing is mock_thing
    try:
        thing()
    except TypeError as err:
        print(f"There was an error {str(err)}")

def using_noncallablemock():

    tmp = object()
    with patch(tmp, new_callable=NonCallableMock) as mock_tmp:
        assert tmp is mock_tmp


def replacing_output():
    def foo():
        print("Hello there")

    @patch("sys.stdout", new_callable=StringIO)
    def test(mock_stdout):
        foo()
        assert mock_stdout.getvalue() == "Hello there\n"

    test()

def main() -> None:
    print(f'Hello main from : {__file__}')
    
    using_noncallablemock()
    
    replacing_output()

if __name__ == '__main__':
    main()