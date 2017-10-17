"""Return nth number of fibonacci and Lucas series."""


def fibonacci(n):
    """Give the nth number in the fibonacci series when given n."""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        print(fibonacci(n - 1) + fibonacci(n - 2))
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return False
