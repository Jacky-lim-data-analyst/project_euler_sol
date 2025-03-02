# how many continued fractions for N <= 10000 have an odd period?
import math

def is_perfect_square(n):
    """Check if n is a perfect square"""
    root = int(math.sqrt(n))
    return root * root == n

def continued_fraction_period(n):
    """Calculate the period of the continued fraction representation of sqrt(n).
    Returns 0 if n is a perfect square (no period), otherwise
    returns the period length.
    
    This uses the algorithm described:
    For sqrt(n), we compute each term in the sequence by manipulating expression of the form:
    (sqrt(n) + b) / c"""
    if is_perfect_square(n):
        return 0    # no period
    
    # initialize the first step
    a0 = int(math.sqrt(n))

    # keep track of the terms we've seen to detect the period
    # each term is uniquely identified by the triple (a, b, c)
    seen_terms = []

    # start with (sqrt(n) - a0) / 1
    b, c = -a0, 1

    while True:
        # calculate the next a, b and c
        # next a_i = floor((sqrt(n) + b) / c)
        a = int((math.sqrt(n) + b) / c)
        
        # store the current state
        current_state = (a, b, c)

        if current_state in seen_terms:
            return len(seen_terms) - seen_terms.index(current_state)
        
        seen_terms.append(current_state)

        new_b = a * c - b

        new_c = (n - new_b**2) // c
        # update
        b, c = new_b, new_c

def count_odd_period_sqrt(limit):
    """Count the number of values N <= limit where sqrt(N) has an odd period"""
    count = 0
    for n in range(2, limit + 1):
        period = continued_fraction_period(n)
        if period > 0 and period % 2 == 1:
            count += 1

    return count

if __name__ == '__main__':
    result = count_odd_period_sqrt(10000)
    print(f"Number of continued fractions for N <= 10000 with odd period: {result}")

    # For verification, let's check the first examples given in the problem
    test_cases = [2, 3, 5, 6, 7, 8, 10, 11, 12, 13]
    for n in test_cases:
        period = continued_fraction_period(n)
        print(f"sqrt({n}) has period {period}")