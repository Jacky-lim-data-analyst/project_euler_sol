# The sum of the squares of the first ten natural numbers is,
# $$1^2 + 2^2 + ... + 10^2 = 385$$
# the square of the sum of the first ten natural numbers is,
# $$(1+2+...+10)^2 = 3025$$

def find_sum_square_difference_first_n(n: int) -> int:
    """Find the difference of the sum of squares of the first n natural numbers and
    the square of the sum
    Args:
        n (int): first n natural numbers

    Returns:
        Difference (int)
        
    Usage examples:
    >>> find_sum_square_difference_first_n(3)
    22
    >>> find_sum_square_difference_first_n(10)
    2640"""
    # sum of squares
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i
    
    # square of sum
    square_of_sum = sum(list(range(1, n + 1))) ** 2

    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("square of sum - sum of squares for first 100 natural numbers:")
    print(find_sum_square_difference_first_n(100))