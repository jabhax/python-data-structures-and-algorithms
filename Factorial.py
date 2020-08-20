''' Find Factorial '''
import time


# Recursive Factorial!
def factorial_recursive(n):
    if n == 1:
        return n
    elif n > 1:
        return n * factorial_recursive(n-1)
    else:
        return 0


# Iterative Factorial!
def factorial_iterative(n):
    prod = 1
    for i in range(n, 1, -1):
        prod *= i
    return prod


# Helper function for calculating end-time from start-time using time.time()
def _et(start_time, tr=10):
    end_time = round(time.time()-start_time, tr)
    start_time = time.time()
    return end_time


def main():
    n = 25
    st = time.time()
    print(f'Iterative: {n}! = {factorial_recursive(n)}\nTook {_et(st)}s')
    st = time.time()
    print(f'Recursive: {n}! = {factorial_iterative(n)}\nTook {_et(st)}s')


if __name__ == '__main__':
    main()
