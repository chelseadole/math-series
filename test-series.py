"""Tests for Fibonacci and Lucas functions"""

FIB_NUMBERS = [
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13)
]

@pytest.mark.parametrize('num, result', FIB_NUMBERS)
def test_fibonacci():
    from series import fibonacci 
    assert fibonacci(num) == result