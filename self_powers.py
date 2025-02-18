# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last 10 digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^{1000}

def last_ten_digits_of_series(upper_limit: int) -> int:
    """Returns the last 10 digits of series
    
    Usage examples:
    >>> last_ten_digits_of_series(10)
    405071317"""
    MOD = 10 ** 10
    total_sum = 0

    for i in range(1, upper_limit + 1):
        total_sum = (total_sum + pow(i, i, MOD)) % MOD

    return total_sum

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    result = last_ten_digits_of_series(1000)
    print(f"The last 10 digits of the series: {result:010d}")