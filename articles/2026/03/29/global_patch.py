# contents of conftest.py
import pytest

# This autouse fixture will be executed for each test function and it will delete
# the method request.session.Session.request so that any attempts within tests to create
# http requests will fail.
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


import functools

# Mind that patching stdlib functions and some third-party libraries used by pytest
# might break pytest itself, therefore in those cases it is recommended to use
# MonkeyPatch.context() to limit the patching to the block you want tested:
def test_partial(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(functools, "partial", 3)
        assert functools.partial == 3