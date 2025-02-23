# In general, $\displaystyle \binom n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ... \times 3 \times 2 \times 1$, and $0! = 1$.
# How many, not necessarily distinct, values of $\displaystyle \binom n r$ for $1 \le n \le 100$, are greater than one-million?

from factorial_sum_digits import calculate_factorial
from collections import namedtuple

def calculate_combination(n: int, r: int) -> int:
    """Calculate combination
    
    Usage example:
    >>> calculate_combination(5, 3)
    10
    >>> calculate_combination(10, 0)
    1
    >>> calculate_combination(10, 5)
    252"""
    if n < 0 or r < 0:
        raise ValueError("n or r cannot be negative.")
    
    denom = calculate_factorial(r) * calculate_factorial(n - r)
    return calculate_factorial(n) // denom

def main():
    nr_pairs = []
    Pair = namedtuple("Pair", "n r")
    for n in range(10, 101):
        for r in range(3, n - 2):
            if calculate_combination(n, r) > 1_000_000:
                pair = Pair(n, r)
                nr_pairs.append(pair)

    return nr_pairs

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    nr = main()

    # print(nr)
    print("The number of values of n and r values: ", len(nr))