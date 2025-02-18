# find all the sum of all numbers which are equal to the sum of the
# factorial of their digits

from factorial_sum_digits import calculate_factorial

def is_sum_digits_equal_sum_factorial(n: int) -> bool:
    """Check whether sum of digits is equal to sum of factorial.
    Args:
        n: int
    Returns:
        bool
    
    >>> is_sum_digits_equal_sum_factorial(145)
    True
    >>> is_sum_digits_equal_sum_factorial(12)
    False"""
    num_str = str(n)
    sum_factorial = sum(calculate_factorial(int(d)) for d in num_str)

    return sum_factorial == n

def main():
    numbers = []
    # 1 and 2 are not counted
    for i in range(3, calculate_factorial(9) * 7):   # the sum of six digit factorial cannot be more than 9! * 7
        if is_sum_digits_equal_sum_factorial(i):
            numbers.append(i)

    return numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    all_numbers = main()
    print(all_numbers)
    print("The sum of all numbers: ", sum(all_numbers))