import time
import random

def set_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_passed = end - start
        print(f'The function {func.__name__} took {time_passed} seconds.')
        return result
    return wrapper

@set_timer
def bubble_sort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]
    return A

@set_timer
def selection_sort(A):
    for i in range(0, len(A) - 1):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
    return A

@set_timer
def insertion_sort(A):
    for i in range(0, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                break
    return A

A = [random.randint(1, 500) for _ in range(9000)]

if __name__=='__main__':
    bubble_sort(A)
    # The function bubble_sort took 1.0315799713134766 seconds.
    insertion_sort(A)
    # The function insertion_sort took 0.01572394371032715 seconds.
    selection_sort(A)
    # The function selection_sort took 1.3273084163665771 seconds.

    # Github: https://github.com/GuiFernandess7