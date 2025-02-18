"""An irrational decimal fraction is created by concatenating the positive
integers:
0.123456789101112...
If d_n represents the nth digit of the fractional part, find the value
of the expression
d_1 x d_10 x ... x d_1000000"""

def output_champernowne_constant(upper_digit_limit: int) -> str:
    """Generate string of fractions
    Args:
        upper_digit_limit: int, number of digit
    Returns:
        String of fractional digits"""
    starting_num = 1
    frac_digit_str = ''
    num_digits = 0
    while num_digits < upper_digit_limit:
        frac_digit_str += str(starting_num)
        starting_num += 1
        num_digits = len(frac_digit_str)

    return frac_digit_str

if __name__ == '__main__':
    idxs = [0, 9, 99, 999, 9999, 99999, 999999]
    champernowne_const = output_champernowne_constant(1_000_000)
    numbers = []
    prod = 1
    for i in idxs:
        const = int(champernowne_const[i])
        numbers.append(int(const))
        prod *= int(const)
    
    print(numbers)
    print("The product: ", prod)