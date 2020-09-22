# Design Patterns

'''
The iterator design pattern falls under the behavioral design patterns category.
Developers come across the iterator pattern in almost every programming
language. This pattern is used in such a way that it helps to access the
elements of a collection (class) in sequential manner without understanding the
underlying layer design.
'''

import time


def fibonacci_generator():
    ''' Fibonacci Generator '''
    # Compute fib(n) = fib(n-2) + fib(n-1) with yield
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i+j

def main():
    # Iterate through Fibonacci Generator
    try:
        n = 1
        for e in fibonacci_generator():
            print(f'n={n}, fib(n)={e}'), time.sleep(1)
            n += 1
    except KeyboardInterrupt:
        print('Calculation Stopped!')


if __name__ == '__main__':
    main()
