# A Pythagorean triplet is a set of 3 natural numbers, a < b < c, for which
# $$a^2 + b^2 = c^2$$
# There exist one Pythagorean triplet for which a + b + c = 1000
# find the product abc.

import math

def find_special_pythagorean_triplet(sum_val: int = 1000) -> list:
    """Find one pythagorean triplet for which a + b + c = sum_val
    Args:
        sum_val: int, default 1000
    
    Returns:
        list of the Pythagorean triplet
    
    Usage examples:
    >>> find_special_pythagorean_triplet(12)
    [3, 4, 5]
    >>> find_special_pythagorean_triplet(30)
    [5, 12, 13]"""

    triplet = None
    for a in range(1, sum_val):
        for b in range(a, sum_val):
            c_squared = a ** 2 + b ** 2
            c = math.isqrt(c_squared)
            if c**2 == c_squared:
                if a + b + c == sum_val:
                    triplet = [a, b, c]
                    break

    return triplet
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    triplet = find_special_pythagorean_triplet()

    if triplet:
        n = 1
        for i in triplet:
            n *= i

    print("The product abc: ", n)