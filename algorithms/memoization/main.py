from fib_with_lru_cache import fibonacci as fib_3
from fibonacci_with_memo import fibonacci as fib_2
from fibonacci_without_memo import fibonacci as fib_1
import time

if __name__=="__main__":
    start = time.time()
    f = fib_2(35)
    end = time.time()

    print(f)
    print(f'Time: {end - start} seconds')