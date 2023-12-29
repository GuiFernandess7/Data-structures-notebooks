from check import check_input

def fibonacci(n):
    check_input(n)
    if n <= 1:
        return n

    result = fibonacci(n - 1) + fibonacci(n - 2)
    return result