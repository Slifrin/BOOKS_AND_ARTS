from unittest.mock import create_autospec, Mock, patch

import tmp_module

def simple_exmaple():
    fake_holidays = Mock(spec=["is_weekday", "get_holidays"])

    fake_holidays.is_weekday()

    try:
        print("before problems")
        fake_holidays.create_event()
    except AttributeError as err:
        print(str(err))


def example_with_spec():
    tmp_module.foo()

    fake_tmp = Mock(spec=tmp_module)

    print(fake_tmp.foo())

def example_with_autospec():
    fake_tmp = create_autospec(tmp_module)
    try:
        print("before problems")
        fake_tmp.create_event()
    except AttributeError as err:
        print(str(err))


def example_with_patch_and_autospec():
    print(f"Calling method from {__name__}")
    with patch(f'{__name__}.tmp_module', autospec=True) as fake_tmp:
        print(fake_tmp.foo())

def main() -> None:
    print(f'Hello main from : {__file__}')
    simple_exmaple()
    example_with_spec()
    example_with_autospec()
    example_with_patch_and_autospec()

if __name__ == '__main__':
    main()