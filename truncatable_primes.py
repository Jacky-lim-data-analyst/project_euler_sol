# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left

from circular_primes import sieve_of_eratosthenes
from largest_prime_factor import is_prime_number

def is_truncatable_primes(n: int) -> bool:
    """Check is a number is truncatable primes
    Args:
        n: int
    Returns:
        boolean, True if truncatable primes
        
    Usage examples:
    >>> is_truncatable_primes(3797)
    True
    >>> is_truncatable_primes(23)
    True
    >>> is_truncatable_primes(11)
    False"""

    n_str = str(n)
    if len(n_str) == 1:
        return False
    
    flag = is_prime_number(n)

    # from right to left
    for i in range(1, len(n_str)):
        truncated_num_rl = n_str[:i]
        truncated_num_lr = n_str[i:]
        if not is_prime_number(int(truncated_num_rl)):
            return False
        
        if not is_prime_number(int(truncated_num_lr)):
            return False
        
    return True if flag else False

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    primes_num = sieve_of_eratosthenes(1_000_000)
    primes_set = set(primes_num)

    truncatable_primes = []
    for i in primes_set:
        if is_truncatable_primes(i):
            truncatable_primes.append(i)

    print(truncatable_primes)
    print("The sum of truncatable primes: ", sum(truncatable_primes))