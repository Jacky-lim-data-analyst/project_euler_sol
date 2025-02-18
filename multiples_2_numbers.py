# If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
# Find the sum of all the multiples of 3 or 5 below 1000

def compute_sum_multiples(threshold: int, *args) -> int:
    """Find and sum up the multiples of numbers in args which are less than
    threshold
    Args:
        threshold (int): upper limit
        args: variable number of arguments

    Returns:
        addition result (int)

    Usage examples:
    >>> compute_sum_multiples(6, 2, 3)
    9
    >>> compute_sum_multiples(10, 3, 5)
    23
    """
    all_multiples = []
    for number in args:
        if number < 0:
            raise ValueError("the values of args cannot be negative.")
        
        multiple = number
        while multiple < threshold:
            all_multiples.append(multiple)
            multiple += number

    return sum(all_multiples)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("Sum of all the multiples of 3 or 5 below 1000")
    print(compute_sum_multiples(1000, 3, 5))