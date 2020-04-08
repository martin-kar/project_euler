"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import numpy as np


def isprime(nbr, known_primes):
    for prime in known_primes:
        if nbr % prime == 0:
            return False
    return True


def get_largest_prime_factor():
    nbr = 1
    number2factorize = 600851475143
    known_primes = np.array([2])
    factors = np.array([])
    while number2factorize > 1:
        nbr += 1
        if isprime(nbr, known_primes):
            known_primes = np.append(known_primes, nbr)
            if number2factorize % nbr == 0:  # If nbr is a prime factor:
                factors = np.append(factors, nbr)
                # This prevents us from checking unnecessarily large
                # values of nbr:
                number2factorize /= nbr
    largest_prime_factor = max(factors)
    return largest_prime_factor


def main():
    largest_prime_factor = get_largest_prime_factor()
    print(largest_prime_factor)


if __name__ == '__main__':
    main()
