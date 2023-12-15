def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_iter(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]


print(fibonacci(40))