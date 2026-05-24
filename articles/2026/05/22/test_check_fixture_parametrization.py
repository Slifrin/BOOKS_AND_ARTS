import pytest
from unittest.mock import patch


import collections


@pytest.fixture
def dummy(request): 
    print(request)
    with patch("collections.Counter"):
        yield

@pytest.mark.parametrize("dummy", [{"a": 1, "b": 2}], indirect=True)
def test_dummy_fix(dummy):
    c = collections.Counter()
    assert c

def test_dummy_fix_simple(dummy):
    c = collections.Counter()
    assert c