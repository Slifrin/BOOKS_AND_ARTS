"""
https://docs.pytest.org/en/stable/example/parametrize.html#indirect-parametrization
"""
import pytest

@pytest.fixture
def fixt(request):
    return request.param * 3

@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert len(fixt) == 3