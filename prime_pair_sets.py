# The primes 3, 7, 109, and 673 are quite remarkable. By taking any 2
# primes, and concatenating them in any order the result will always be 
# prime. 
# Find the lowest sum for a set of five primes for which any 2 primes 
# concatenate to produce another prime.

from circular_primes import sieve_of_eratosthenes
import math
from functools import lru_cache
from itertools import combinations

def is_prime(n):
    # handle small numbers and even numbers
    if n <= 1:
        return False
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # check for factors from 5 to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# concatenate numbers
def concat_numbers(a: int, b: int) -> int:
    """Concatenate two integers mathematically"""
    # compute number of digits in b
    digits = int(math.log10(b)) + 1
    return a * (10 ** digits) + b

@lru_cache
def is_concat_prime(a: int, b: int) -> bool:
    """Return whether the concatenation of a and b is prime."""
    return is_prime(concat_numbers(a, b))

def is_valid_set(prime_set: tuple[int, ...]) -> bool:
    """Check that every pair of primes in the set concatenate in both orders form a prime number."""
    for a, b in combinations(prime_set, 2):
        if not (is_concat_prime(a, b) and is_concat_prime(b, a)):
            return False
        
    return True

def find_lowest_sum_set_of_primes():
    n = 5
    limit = 10_000
    primes = sieve_of_eratosthenes(limit)

    best_set = None
    min_sum = float('inf')

    for prime_combo in combinations(primes, n):
        if is_valid_set(prime_combo):
            current_sum = sum(prime_combo)
            if current_sum < min_sum:
                min_sum = current_sum
                best_set = prime_combo

    return best_set, min_sum

if __name__ == '__main__':
    best_set, min_sum = find_lowest_sum_set_of_primes()
    print(f"The lowest sum for a set of five primes is {min_sum} with the set {best_set}")
