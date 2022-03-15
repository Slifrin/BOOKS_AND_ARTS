"""
https://realpython.com/python-lambda/#monkey-patching
"""

from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f"TOKEN_{secrets.token_hex(8)}"


@contextmanager
def mock_token():
    """
        Context manager to monkey patch the secrets.token_hex
        function during testing.
    """

    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_bytes = default_token_hex

def test_gen_key():
    """Test the random token."""
    with mock_token():
        print(gen_token() == f"TOKEN_{'feedfacecafebeef'}")
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_key()

import functools

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
reduction_output = functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
print(reduction_output)

alternative_output = sum(x[0] for x in pairs)
print(alternative_output)
