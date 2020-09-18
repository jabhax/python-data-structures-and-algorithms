def count_primes(n: int) -> int:
    # Prime Sieve of Eratosthenes
    if n < 2: return 0
    sieve = prime_sieve(n)
    return len([i for i in sieve if i])

def convert_to_binary(sieve: list) -> list:
    # Convert Prime Sieve list from 'True'/'False' to '0'/'1'
    return [1 if i else 0 for i in sieve]

def prime_sieve(n: int) -> list:
    # Prime Sieve of Eratosthenes
    sieve, sqrt = [True]*n, int(n**(0.5))
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes.
    for i in range(2, sqrt+1):
        p = i*2
        while p < n:
            sieve[p] = False
            p += i
    return sieve

def main():
    n = 25
    sieve = prime_sieve(n)
    print(f'n: { n }')
    print(f'sieve: { sieve }')
    print(f'binary_sieve: { convert_to_binary(sieve) }')
    print(f'count_primes: { count_primes(n) }')


if __name__ == '__main__':
    main()
