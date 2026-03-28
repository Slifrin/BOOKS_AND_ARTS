import pytest

def test_db_initialized(db):
    # dummy test
    if db.__class__.__name__ == "DB2":
        pytest.fail("deliberately failing for demo purposes")
