# 1 / 6 = 0.1(6) means 0.16666..., and has a 1-digit recurring cycle.
# 1 / 7 = 0.(142857), has a 6-digit recurring cycle.

def find_n_digit_recurring_cycle(numerator: int, denominator: int) -> tuple:
    """Returns the n-digit recurring cycle of the fraction numerator/denominator
    Args:
        numerator: int
        denominator: int
    Returns:
        int, number of digits recurring cycle
        
    # Usage examples:
    # >>> find_n_digit_recurring_cycle(1, 2)
    # 0
    # >>> find_n_digit_recurring_cycle(1, 3)
    # 1
    # >>> find_n_digit_recurring_cycle(1, 7)
    # 6"""
    # dictionary to store remainder and its corresponding positions
    remainder_positions = {}
    digits = []

    # start with the initial remainder 
    remainder = numerator % denominator

    while remainder != 0 and remainder not in remainder_positions:
        # record the position of this remainder.
        remainder_positions[remainder] = len(digits)

        # multiply the remainder by 10 to simulate division
        remainder *= 10
        # the next digit in the decimal expansion
        digit = remainder // denominator
        digits.append(str(digit))

        # update the remainder
        remainder %= denominator

    # if remainder is 0, the fraction terminates
    if remainder == 0:
        return 0, None
    else:
        start_index = remainder_positions[remainder]
        return (len(digits[start_index:]), start_index)
    
def main():
    max_num_digits = 0
    d = None
    start_index = None
    for i in range(2, 1000):
        n_digit_cycle = find_n_digit_recurring_cycle(1, i)[0]
        if n_digit_cycle > max_num_digits:
            max_num_digits = n_digit_cycle
            d = i
            start_index = find_n_digit_recurring_cycle(1, i)[1]

    print(f"1 / {d} contain the longest recurring cycle: {max_num_digits} starting at {start_index}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()