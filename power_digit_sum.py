# sum of digits of the number 2^1000

def sum_of_digits_of_power_of_two(n: int) -> int:
    """Returns the sum of the digits of 2^n.
    Args:
        n: int, 2^n
    Returns:
        int, sum of digits
        
    Usage examples:
    >>> sum_of_digits_of_power_of_two(5)
    5
    >>> sum_of_digits_of_power_of_two(15)
    26"""
    return sum(int(digit) for digit in str(2 ** n))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(f"sum of digits for 2^{1000}: {sum_of_digits_of_power_of_two(1_000)}")