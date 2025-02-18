# $2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.
# What is the smallest positive number that is evenly divisible divisible with no remainder by all the numbers from
# 1 to 20?

# Relationship between LCM and GCD
# $LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}$

import math
from functools import reduce

# Note for functools.reduce()
# 1. Apply a function (or callable) to the first 2 items in an iterable and 
# generate a partial result.
# 2. Use that partial result, together with the third item in the iterable,
# to generate another partial result
# 3. Repeat the process until the iterable is exhausted.

def lcm(n1: int, n2: int) -> int:
    """Calculate the lowest common multiple (LCM) of 2 numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The LCM of the 2 numbers
        
    Usage examples:
    >>> lcm(2, 3)
    6
    >>> lcm(4, 5)
    20"""
    return int(abs(n1 * n2) / math.gcd(n1, n2))

def lcm_of_range(lower: int, upper: int) -> int:
    """Calculate the lowest common multiple (LCM) of a range of numbers.
    
    Args:
        lower (int): the lower bound of the range (inclusive)
        upper (int): the upper bound of the range (inclusive)
        
    Returns:
        int: the LCM of the range of numbers
        
    Usage examples:
    >>> lcm_of_range(1, 4)
    12
    >>> lcm_of_range(4, 6)
    60"""
    if lower >= upper:
        raise ValueError("The lower input cannot be greater or equal to upper input")
    return reduce(lcm, range(lower, upper + 1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Smallest positive number that is divisible by each number from 1 to 10: ")
    print("-"*30)
    print(lcm_of_range(1, 10))
    print()
    print("Smallest positive number that is divisible by each number from 1 to 20: ")
    print("-"*30)
    print(lcm_of_range(1, 20))