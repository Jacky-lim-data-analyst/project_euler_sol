# By listing first 6 prime numbers: 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13
# What is the nth prime number?

from largest_prime_factor import is_prime_number

def find_nth_prime_number(n: int) -> int:
    """Find the first n prime number
    Args:
        n (int): number of prime number
    
    Returns:
        int: the first nth prime number
        
    Usage examples:
    >>> find_nth_prime_number(2)
    3
    >>> find_nth_prime_number(6)
    13"""
    prime_number_tracker = 0
    starting_integer = 1
    while prime_number_tracker < n:
        starting_integer += 1
        if is_prime_number(starting_integer):
            prime_number_tracker += 1
        
    return starting_integer

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("The 10,001st prime number: ", find_nth_prime_number(10_001))