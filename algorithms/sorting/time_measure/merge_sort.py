import sys
import time

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
def merge_sort(A):
    merge_sort_2(A, 0, len(A) - 1)

def merge_sort_2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort_2(A, first, middle)
        merge_sort_2(A, middle + 1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    left = A[first:middle + 1]
    right = A[middle + 1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    top_right = top_left = 0

    for k in range(first, last + 1):
        if left[top_left] < right[top_right]:
            A[k] = left[top_left]
            top_left += 1
        else:
            A[k] = right[top_right]
            top_right += 1

#A = [random.randint(1, 500) for _ in range(9000)]
A = [6, 5, 3, 1, 8, 7, 2, 4]
print(A)
merge_sort(A)
print(A)