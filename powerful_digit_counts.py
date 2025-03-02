# The 5-digit number, 16807 = 7^5. Similarly, the 9-digit number
# 134217728 = 8^9 is a ninth power.
# How many n-digit positive integers exist which are also
# an nth power?

def num_n_digit_int(n: int) -> int:
    """Return the number of n-digit integers which are also
    an nth power
    
    >>> num_n_digit_int(1)
    9
    >>> num_n_digit_int(3)
    5
    >>> num_n_digit_int(4)
    4"""
    if n <= 0:
        raise ValueError("n must be positive.")

    integers = set()
    for i in range(1, 10):
        power_of_i = pow(i, n)
        if 10**(n-1) <= power_of_i < 10**n:
            integers.add((i, n, power_of_i))
        else:
            continue

    return len(integers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()