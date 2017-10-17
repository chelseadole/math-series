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
    (7, 13),
    (8, 21),
    (9, 34)
]

LUCAS_NUMBERS = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47),
    (9, 76)
]


def test_fib_import():
    """Test if series imports."""
    from series import fibonacci


@pytest.mark.parametrize('n, result', FIB_NUMBERS)
def test_fibonacci(n, result):
    """Test for fibonacci sequence."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_NUMBERS)
def test_lucas(n, result):
    """Test for lucas sequence."""
    from series import lucas
    assert lucas(n) == result


def test_sum_series(n, op1, op2):
    """Test the sum function."""
    from series import fibonacci
    from series import lucas
    from series import sum_series
    if op1 == 0 and op2 == 1:
        test_fibonacci(n)
    elif op1 == 2 and op2 == 1:
        test_lucas(n)
    else:
        assert sum_series(n) == sum_series(n - 1) + sum_series(n - 2)
