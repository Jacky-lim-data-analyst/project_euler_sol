# Find the sum of digits in the numerator of the 100th convergent
# of continued fraction for e.

from fractions import Fraction

def continued_fraction_e(n_terms: int) -> list:
    """
    Generate the first `n_terms` of the continued fraction representation of e.
    Args:
        n_terms: Number of terms to generate
    Returns:
        List of terms in the continued fraction of e"""
    cf = [2]  # the first term of the continued fraction of e

    for k in range(1, n_terms):
        if k % 3 == 2:
            cf.append(2 * (k // 3 + 1))   # Every third term 
        else:
            cf.append(1)

    return cf

def cont_frac_fraction_e(depth: int, continued_frac: list) -> Fraction:
    """Recursive function
    Args:
        depth: int, the precision of approximation
    Return:
        Fraction, approximated value"""
    sum_ = Fraction(continued_frac[0], 1)
    
    for i in range(1, depth):
        sum_ = sum_ + Fraction(1, 1) / continued_frac[i]

    return sum_

def main():
    e_conv_list = continued_fraction_e(1000)

    e_convergent = cont_frac_fraction_e(1000, e_conv_list)

    str_numerator = str(e_convergent.numerator)
    # print(str_numerator)
    return sum([int(i) for i in str_numerator])

if __name__ == '__main__':
    print(main())