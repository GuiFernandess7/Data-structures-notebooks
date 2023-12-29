from functools import lru_cache
from check import check_input

@lru_cache(maxsize=1000)
def fibonacci(n):
    check_input(n)
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))
