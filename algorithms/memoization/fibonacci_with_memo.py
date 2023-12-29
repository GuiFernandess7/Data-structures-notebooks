from check import check_input

def fibonacci(n, memo=None):
    check_input(n)
    if memo is None:
        memo = {}

    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]