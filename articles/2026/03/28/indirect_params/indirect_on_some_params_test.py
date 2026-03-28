import pytest


@pytest.fixture(scope="function")
def x(request: pytest.FixtureRequest):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request: pytest.FixtureRequest):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"
