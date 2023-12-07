def recursion(n):
    if n > 5:
        n - 1
        return n * recursion(n - 1)
    else:
        return n

print(recursion(6))