import pytest

from implementation import Base, Implementation, DerivedList


def test_abstract_base_class():
    with pytest.raises(TypeError):
        Base()


def test_implementation():
    instance = Implementation('Hello', 'There')
    assert isinstance(instance, Base)
    assert instance.process() == 'HELLO there'


def test_custom_list():
    instance = DerivedList(['Hello', 'there'])

    for element in ['Hello', 'there']:
        assert element in instance

    assert instance.capitalize() == ['HELLO', 'THERE']