import unittest
from enum import Enum
from unittest.mock import patch

from sumbodule import MyEnumMeta, Color, foo


class DummyColor(Enum, metaclass=MyEnumMeta):
    TEST_TYPE1 = 1
    TEST_TYPE2 = 10


class MyTest(unittest.TestCase):

    # def test_a(self):
    #     assert foo("RED") == "valid"
    #     assert foo("YELLOW") == "invalid"


    # @patch('__main__.Color', DummyColor)
    @patch('sumbodule.Color', DummyColor)
    def test_b(self):
        assert foo("TEST_TYPE1") == "valid"
        assert foo("TEST_TYPE10") == "invalid"


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)