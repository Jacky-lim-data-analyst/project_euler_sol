# The prime factors of $13195$ are $5, 7, 13$ and $29$.
# What is the largest prime factor of the number $600851475143$?

import math

def is_prime_number(number: int) -> bool:
    """Check if a given number is a prime number.
    Args:
        number (int)
    Returns:
        Flag (boolean)
        
    Usage examples:
    >>> is_prime_number(0)
    False
    >>> is_prime_number(1)
    False
    >>> is_prime_number(11)
    True
    >>> is_prime_number(2)
    True
    >>> is_prime_number(24)
    False"""

    if number < 0:
        raise ValueError("input parameter cannot be negative")
    
    if number in (0, 1):
        return False

    N = int(math.sqrt(number)) + 1
    for i in range(2, N):
        if number % i == 0:
            return False
        
    return True

def find_prime_factors(number: int) -> list:
    """Returns a list of prime factors.
    Args:
        number (int)
    Returns:
        a list of prime factors (list)
    
    Usage examples:
    >>> find_prime_factors(10)
    [2, 5]
    >>> find_prime_factors(13195)
    [5, 7, 13, 29]
    >>> find_prime_factors(1)
    []
    >>> find_prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer."""
    if number <= 0:
        raise ValueError("Input must be a positive integer.")
    return [i for i in range(1, number + 1) if number % i == 0 and \
            is_prime_number(i)]

def find_largest_prime_factor(number: int) -> int:
    """Returns a list of prime factors.
    Args:
        number (int)
    Returns:
        a maximum prime factor (int)
    
    Usage examples:
    >>> find_largest_prime_factor(2)
    2
    >>> find_largest_prime_factor(20)
    5
    >>> find_largest_prime_factor(1)
    Traceback (most recent call last):
        ...
    ValueError: No prime factor for the given input."""
    if number <= 1:
        raise ValueError("No prime factor for the given input.")

    max_prime_factor = None
    for i in range(1, number + 1):
        if number % i == 0 and is_prime_number(i):
            max_prime_factor = i

    return max_prime_factor

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("The largest prime factor: ", end="")
    print(find_largest_prime_factor(13_195))