"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.
What is the 10 001st prime number?
"""

REQUIRED_PRIME_INDEX = 10001


def is_prime(nbr, stored_primes):
    for prime in stored_primes:
        if prime ** 2 > nbr:
            return True
        if nbr % prime == 0:
            return False
    return True


def get_prime_number():
    stored_primes = [2, 3]
    nbr = 3
    while len(stored_primes) < REQUIRED_PRIME_INDEX:
        nbr += 2
        if is_prime(nbr, stored_primes):
            stored_primes.append(nbr)
    return stored_primes[-1]


print(get_prime_number())
