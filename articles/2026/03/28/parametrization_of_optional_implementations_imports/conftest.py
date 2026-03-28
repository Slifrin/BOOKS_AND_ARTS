"""
If you want to compare the outcomes of several implementations of a given
API, you can write test functions that receive the already imported implementations
and get skipped in case the implementation is not importable/available.
Let’s say we have a “base” implementation and the other (possibly optimized ones)
need to provide similar results:
"""

import pytest

@pytest.fixture(scope="session")
def basemod(request: pytest.FixtureRequest):
    return pytest.importorskip("base")

@pytest.fixture(scope="session", params=["opt1", "opt2"])
def optmod(request: pytest.FixtureRequest):
    return pytest.importorskip(request.param)
