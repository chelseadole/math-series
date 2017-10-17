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
    (9, 34),
    (-1, False),
    (-200, False),
    (30, 832040),
    (13, 233)
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
    (9, 76),
    (-1, False),
    (-200, False),
    (17, 3571),
    (23, 64079)
]

SUM_NUMBERS = [
    (0, 0, 1, 0),
    (1, 0, 1, 1),
    (2, 0, 1, 1),
    (3, 0, 1, 2),
    (9, 0, 1, 34),
    (15, 0, 1, 610),
    (-12, 0, 1, False),
    (0, 2, 1, 2),
    (1, 2, 1, 1),
    (2, 2, 1, 3),
    (3, 2, 1, 4),
    (8, 2, 1, 47),
    (23, 2, 1, 64079),
    (-1, 2, 1, False),
    (0, 5, 4, 5),
    (3, 5, 4, 13),
    (0, 13, 1, 13),
    (1, 13, 1, 1),
    (4, 13, 1, 29),
    (0, 3, 2, 3),
    (1, 3, 2, 2),
    (4, 3, 2, 12),
    (-3, 5, 2, False),
    (15, 5, 3, 3715),
    (13, 1, 3, 843)
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


@pytest.mark.parametrize('n, op1, op2, result', SUM_NUMBERS)
def test_sum_series(n, op1, op2, result):
    """Test the sum function."""
    from series import sum_series
    assert sum_series(n, op1, op2) == result
