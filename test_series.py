"""Tests for Fibonacci and Lucas functions."""


import pytest


FIB_NUMBERS = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
]


def test_fib_import():
    """Test if series imports."""
    from series import fibonacci


@pytest.mark.parametrize('n, result', FIB_NUMBERS)
def test_fibonacci(n, result):
    """Test for fibonacci sequence."""
    from series import fibonacci
    assert fibonacci(n) == result
