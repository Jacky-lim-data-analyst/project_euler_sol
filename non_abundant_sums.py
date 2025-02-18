# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# a number n is called deficient if the sum of its proper divisors is less than n and it is called
# abundant if this sum exceeds n.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum 
# of 2 abundant numbers.

# UPPER_LIMIT = 28_123

def sum_of_proper_divisors(n: int) -> int:
    """Return the sum of proper divisors of n.
    
    Usage examples:
    >>> sum_of_proper_divisors(28)
    28
    >>> sum_of_proper_divisors(29)
    1"""
    if n == 1:
        return 0
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors

def is_abundant_number(n: int) -> bool:
    """Check if n is an abundant number
    
    Usage examples:
    >>> is_abundant_number(12)
    True
    >>> is_abundant_number(13)
    False"""
    return sum_of_proper_divisors(n) > n

def find_abundant_numbers(upper_limit: int) -> list:
    """Return a list of abundant numbers up to a given limit."""
    return [n for n in range(1, upper_limit + 1) if is_abundant_number(n)]

def is_sum_of_two_abundant(n: int, abundant_numbers: list) -> bool:
    """Check if n can be written as the sum of 2 abundant numbers.
    
    Usage examples:
    >>> is_sum_of_two_abundant(24, [12])
    True"""
    for a in abundant_numbers:
        if a >= n:
            break
        if (n - a) in abundant_numbers:
            return True
    return False

def sum_of_two_non_abundant(limit: int) -> int:
    """Return the sum of all positive integers up to the limit that cannot be written as the sum of
    abundant numbers"""
    abundant_numbers = find_abundant_numbers(limit)
    non_sum_numbers = [n for n in range(1, limit + 1) if not is_sum_of_two_abundant(n, abundant_numbers)]
    return sum(non_sum_numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    UPPER_LIMIT = 28_123
    result = sum_of_two_non_abundant(UPPER_LIMIT)
    print("the sum of all positive integers up to the limit that cannot be written as the sum of abundant numbers: ")
    print(result)