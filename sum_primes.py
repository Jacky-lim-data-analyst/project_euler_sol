# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# find the sum of all the primes below 2_000_000

from largest_prime_factor import is_prime_number

def sum_primes(threshold: int) -> int:
    """Find the sum of all primes below threshold.
    Args:
        threshold: int, upper limit
    
    Returns:
        Sum of primes number below threshold
        
    Usage examples:
    >>> sum_primes(10)
    17
    >>> sum_primes(20)
    77"""

    if threshold < 2:
        return 0
    
    accumulator = 0
    for i in range(2, threshold):
        if is_prime_number(i):
            accumulator += i

    return accumulator

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Sum of all primes below 2 million: ", sum_primes(2_000_000))
