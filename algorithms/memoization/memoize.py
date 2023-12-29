from functools import wraps
from check import check_input

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper

@memoize
def fibonacci(n):
    check_input(n)
    if n <= 1:
        return n

    result = fibonacci(n - 1) + fibonacci(n - 2)
    return result