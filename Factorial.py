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


def main():
    n = 10
    print(f'Iterative: {n}! = {factorial_recursive(n)}')
    print(f'Recursive: {n}! = {factorial_iterative(n)}')

if __name__ == '__main__':
    main()
