import pytest


def pytest_generate_tests(metafunc):
    if "db" in metafunc.fixturenames:
        metafunc.parametrize("db", ["d1", "d2"], indirect=True)

class DB1:
    "One database object"

class DB2:
    "Alternative database object"

@pytest.fixture
def db(request: pytest.FixtureRequest):
    if request.param == "d1":
        return DB1()
    if request.param == "d2":
        return DB2()
    else:
        return ValueError("Invalid internal test config")