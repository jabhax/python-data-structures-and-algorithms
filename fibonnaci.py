''' Fibonnaci '''
import time
import json


# Fibonnaci using Iterative Solution WITH NO Dynamic Programming / Caching
def fibonnaci_iterative(n):
    sum, n1, n2 = 0, 1, 0
    for i in range(n):
        sum = n1 + n2
        n2 = n1
        n1 = sum
    return sum


# Fibonnaci using Recursive Solution WITH NO Dynamic Programming / Caching
def fibonnaci_slow(n):
    return n if n < 2 else (fibonnaci_slow(n-1) + fibonnaci_slow(n-2))


# Fibonnaci using Recursive Solution WITH Dynamic Programming / Caching using
# hash_table/dictionary structures
def fibonnaci_fast(n, t):
    if n in t:
        return t[n]
    t[n] = n if n < 2 else (fibonnaci_fast(n-1, t) + fibonnaci_fast(n-2, t))
    return t[n]


# Helper function for calculating end-time from start-time using time.time()
def _et(start_time, tr=8):
    end_time = round(time.time()-start_time, tr)
    start_time = time.time()
    return end_time


def main():
    n, fast_fib, slow_fib, iter_fib = 30, {}, {}, {}
    # Test all Fibonnaci-Fast sequences from [0, n]
    st = time.time()
    hash_table = {}
    print('Fibonnaci-Fast...')
    for i in range(n+1):
        fast_fib[i] = fibonnaci_fast(i, hash_table)
    print(f'[n: fib(n)] = {json.dumps(fast_fib, indent=4)}')
    print(f'Time for fibonnaci_fast: {_et(st)}\n')
    # Test all Fibonnaci-Iterative sequences from [0, n]
    st = time.time()
    print('Fibonnaci-Iterative...')
    for i in range(n+1):
        iter_fib[i] = fibonnaci_iterative(i)
    print(f'[n: fib(n)] = {json.dumps(iter_fib, indent=4)}')
    print(f'Time for fibonnaci_iterative: {_et(st)}\n')
    # Test all Fibonnaci-Slow sequences from [0, n]
    # NOTE: IF this hangs the program, lower the value of N and try again.
    st = time.time()
    print('Fibonnaci-Slow...')
    for i in range(n+1):
        slow_fib[i] = fibonnaci_slow(i)
    print(f'[n: fib(n)] = {json.dumps(slow_fib, indent=4)}')
    print(f'Time for fibonnaci_slow: {_et(st)}\n')


if __name__ == '__main__':
    main()
