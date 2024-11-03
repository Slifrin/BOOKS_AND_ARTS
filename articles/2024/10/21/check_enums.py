from enum import Enum
from unittest.mock import patch

from fake_enum_test import Action, use_hello
from instantiatie_dummy import create_dummy_instance_and_call_f


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def check_enum_patch():
    with patch("fake_enum_test.hello") as hello_mock:
        print(Action.HELLO())
        use_hello()
        try:
            print(Action(2))
        except ValueError as err:
            print(str(err))

        member = Action.HELLO

        member()
        print(type(member))
        # print(member.value)

        # print(Action["HELLO"])


def other_check():
    # with patch("fake_enum_test.dummy_class.DummyClass", autospec=True) as dummy_f_mock:
    # with patch("fake_enum_test.dummy_class.DummyClass.f") as dummy_f_mock:
    with patch("fake_enum_test.dummy_class.DummyClass.f") as dummy_f_mock:
        create_dummy_instance_and_call_f()

    dummy_f_mock.assert_called_once()


def main() -> None:
    print(f"Hello main from : {__file__}")
    Action.HELLO()
    Color.BLUE
    # check_enum_patch()

    other_check()


if __name__ == "__main__":
    main()
