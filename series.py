"""Return nth number of fibonacci and Lucas series."""


def fibonacci(n):
    """Give the nth number in the fibonacci series when given n."""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return False

def lucas(n):
    """Give the nth number in the lucas series when given n."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n - 1) + lucas(n - 2)
    else:
        return False

def sum_series(n, op1 = 0, op2 = 1):
    """Create new series based on op1 and op2 inputs"""
    if op1 == 0 and op2 == 1:
        return fibonacci(n)
    elif op1 == 2 and op2 == 1:
        return lucas(n)
    else:
        if n == 0:
            return op1
        elif n == 1:
            return op2
        else: 
            return sum_series(n - 1) + sum_series(n - 2)

