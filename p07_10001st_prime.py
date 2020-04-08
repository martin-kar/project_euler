"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(nbr, stored_primes):
    for prime in stored_primes:
        if nbr % prime == 0:
            return False
    return True


def get_prime_number():
    stored_primes = [2]
    nbr = 2
    while len(stored_primes) <= 10000:
        nbr += 1
        if is_prime(nbr, stored_primes):
            stored_primes.extend([nbr])
    return stored_primes[-1]


print(get_prime_number())
