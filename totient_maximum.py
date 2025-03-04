"""Euler's totient function, phi function is defined as 
the number of positive integers not exceeding n which are
relatively prime to n.
Find the value of n <= 1,000,000 for which n / phi(n) is a
maximum"""

import math

def phi(n: int) -> int:
    """Euler tiotient function
    
    >>> phi(2)
    1
    >>> phi(10)
    4"""
    res = 0
    i = 1
    while i < n:
        if math.gcd(i, n) == 1:
            res += 1

        i += 1

    return res

def main():
    max_n_per_phi = 0
    max_n = 0
    for n in range(2, 1_000_001):
        # evaluate n per phi
        try:
            npp = n / phi(n)
        except ZeroDivisionError as e:
            print(e)

        if npp > max_n_per_phi:
            max_n_per_phi = npp
            max_n = n

    return max_n


if __name__ == '__main__':
    print(__doc__)
    import doctest
    doctest.testmod()

    max_n = main()
    print("The value for which n / phi(n) is maximum: ", max_n)