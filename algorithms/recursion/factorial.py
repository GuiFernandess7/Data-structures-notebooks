def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Iterable way
def iterable_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iterable_factorial(5))