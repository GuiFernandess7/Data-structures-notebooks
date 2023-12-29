from fib_with_lru_cache import fibonacci as fib_3
from fibonacci_with_memo import fibonacci as fib_2
from fibonacci_without_memo import fibonacci as fib_1
from memoize import fibonacci as fib_4
from time import perf_counter

def measure_fibonacci_time(func, n):
    start = perf_counter()
    result = func(n)
    end = perf_counter()
    print(f'Time: {end - start} seconds')
    return result

if __name__=="__main__":
    value = 34

    result = measure_fibonacci_time(fib_1, value)
    print(result)

    result_2 = measure_fibonacci_time(fib_2, value)
    print(result_2)

    result_3 = measure_fibonacci_time(fib_3, value)
    print(result_3)

    result_4 = measure_fibonacci_time(fib_4, value)
    print(result_4)

"""
Results:

Time: 2.5200573000001896 seconds
5702887
Time: 5.830000009154901e-05 seconds
5702887
Time: 1.3899996702093631e-05 seconds
5702887
Time: 0.00010459999975864775 seconds
5702887 """