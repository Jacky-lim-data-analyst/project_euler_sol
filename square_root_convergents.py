# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# $\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$
# By expanding this for the first four iterations, we get:
# <p>$1 + \frac 1 2 = \frac  32 = 1.5$<br>
# $1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br>
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br>
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br></p>
# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than the denominator?

from fractions import Fraction

def cont_frac_fraction(depth: int) -> Fraction:
    """Recursive function
    Args:
        depth: int, the precision of approximation
    Return:
        Fraction, approximated value
        
    >>> cont_frac_fraction(1)
    Fraction(5, 2)
    >>> cont_frac_fraction(3)
    Fraction(29, 12)"""
    result = Fraction(2, 1)
    for _ in range(depth):
        result = Fraction(2, 1) + Fraction(1, 1) / result
    return result

def approx_sqrt2_fraction(depth: int) -> Fraction:
    """Approximate sqrt(2) as a fraction using the continued fraction representation:
        sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))
    Args:
        depth: int, the number of recursive iterations.
    Returns:
        Fractions
        
    >>> approx_sqrt2_fraction(1)
    Fraction(7, 5)"""
    return Fraction(1, 1) + Fraction(1, 1) / cont_frac_fraction(depth)

def main():
    count = 0
    for i in range(1, 1001):
        frac = approx_sqrt2_fraction(i)
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            count += 1

    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("# of fractions contain a numerator with more digits than denominator: \n")
    print(main())