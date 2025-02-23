# A googol (10^100) is a massive number: one followed by one-hundred zeros.
# Despite the size, the sum of the digits in each number is only 1.
# considering natural numbers of the form, a^b where a, b < 100, what
# is maximum digital sum?

def sum_of_digits(n: int) -> int:
    """compute the sum of digits in a given number.
    
    >>> sum_of_digits(6)
    6
    >>> sum_of_digits(100000)
    1
    >>> sum_of_digits(4321)
    10"""
    return sum([int(i) for i in str(n)])

def main():
    max_sum_val = 0
    num_with_max_sum_digits = None
    for a in range(1, 100):
        for b in range(1, 100):
            res = a ** b
            sod = sum_of_digits(res)
            if max_sum_val < sod:
                max_sum_val = sod
                num_with_max_sum_digits = (a, b)

    return max_sum_val, num_with_max_sum_digits

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    max_sum_val, ab = main()
    print("Maximum digital sum: ", max_sum_val)
    print(ab)