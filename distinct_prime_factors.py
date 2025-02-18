# the first two consecutive numbers to have two distinct prime factors 
# are:
# 14 = 2 * 7
# 15 = 3 * 5
# Find the first four consecutive integers to have 4 distinct prime factors
# each. What is the first of these numbers?

def has_k_distinct_prime_factors(n: int, k: int) -> bool:
    """
    Returns True if n has exactly k distinct prime factors, False otherwise.
    
    Usage examples:
    >>> has_k_distinct_prime_factors(14, 2)
    True
    >>> has_k_distinct_prime_factors(3, 2)
    False
    >>> has_k_distinct_prime_factors(644, 3)
    True"""
    if n < 2: 
        return False
    
    count = 0
    factor = 2
    # check potential factors up to sqrt(n)
    while factor * factor <= n:
        if n % factor == 0:
            count += 1

        # remove all occurrences of this factor
        while n % factor == 0:
            n //= factor

        # early exit if we already have more than k factors
        if count > k:
            return False
        
        factor += 1

    # If there is a remaining factor greater than sqrt(n), count
    if n > 1:
        count += 1
    
    return count == k

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    window_size = 4
    max_int = 300_000
    for i in range(645, max_int - window_size + 1):
        consecutive_nums = [i + ws for ws in range(window_size)]

        flags = [has_k_distinct_prime_factors(n, 4) for n in consecutive_nums]

        if all(flags):
            print("The first 4 consecutive integers: ", consecutive_nums)
            break
    
    if not all(flags):
        print("Not found.")
