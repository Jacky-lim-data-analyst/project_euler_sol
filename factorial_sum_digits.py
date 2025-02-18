# find the sum of the digits in the number 100!

def calculate_factorial(n):
    """Calculate factorial of n.
    Args:
        n: int, n!
    Returns:
        int, result of factorial

    Usage examples:    
    >>> calculate_factorial(3)
    6
    >>> calculate_factorial(5)
    120"""
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    
    if n in (0, 1):
        return 1
    
    return n * calculate_factorial(n - 1)

def sum_of_digits(num_str: str) -> int:
    """Compute the sum of digits.
    Args:
        num_str: str, number
    Returns:
        int, sum of digits
        
    Usage examples:
    >>> sum_of_digits('345')
    12
    >>> sum_of_digits('14500')
    10"""
    if not num_str.isdecimal():
        raise ValueError("input must only be numbers")
    
    sum_ = 0
    for num in num_str:
        sum_ += int(num)

    return sum_

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Sum of digits in the number 100!")
    print(sum_of_digits(str(calculate_factorial(100))))