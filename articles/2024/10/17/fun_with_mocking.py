"""
https://stackoverflow.com/questions/1289894/how-do-i-mock-an-open-used-in-a-with-statement-using-the-mock-framework-in-pyth
https://docs.python.org/3/library/unittest.mock.html#patch
"""

from unittest.mock import mock_open, patch


def check_mock_open():
    m = mock_open()

    with patch('__main__.open', m):
        with open('foo', 'w') as h:
            h.write('some stuff')

    print(m.mock_calls)
    m.assert_called_once_with('foo', 'w')
    handle = m()
    handle.write.assert_called_once_with('some stuff')


def check_write_to_mock_open():
    print(f'Running {check_write_to_mock_open.__name__}')
    
    with patch('__main__.open', mock_open(read_data='bibble')) as m:
        with open('foo') as h:
            result = h.read()

    m.assert_called_once_with('foo')
    assert result == 'bibble'

def other_use_of_patch():
    print(f'Running {other_use_of_patch.__name__}')

    @patch('builtins.open', new_callable=mock_open, read_data='dummy_data')
    def check_patch(mock_file):
        assert open('path/to/open').read() == 'dummy_data'
        mock_file.assert_called_with('path/to/open')

    check_patch()


def main() -> None:
    print(f'Hello main from : {__file__}')

    check_mock_open()
    check_write_to_mock_open()
    other_use_of_patch()

if __name__ == '__main__':
    main()