# evaluate all the amicable numbers under 10000
# proper divisor is any positive divisor of that number that is not the
# number itself.

def calc_sum_of_proper_divisors(n: int) -> int:
    """Sum of proper divisors.
    Args:
        n: int
    Returns:
        sum of proper divisors
    
    >>> calc_sum_of_proper_divisors(6)
    6
    >>> calc_sum_of_proper_divisors(7)
    1"""
    return sum([i for i in range(1, n) if n % i == 0])

def main():
    amicable_numbers = []
    amicable_number_set = set()
    for number in range(2, 10_000):
        spd = calc_sum_of_proper_divisors(number)
        spd_converse = calc_sum_of_proper_divisors(spd)
        if spd_converse == number and number != spd:
            amicable_numbers.append((number, spd))
            amicable_number_set.add(number)
            amicable_number_set.add(spd)

    print("Possible amicable numbers:")
    print(amicable_numbers)
    print("Sum of amicable numbers:")
    print(amicable_number_set)
    print(sum(amicable_number_set))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
