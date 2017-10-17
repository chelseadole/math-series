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
