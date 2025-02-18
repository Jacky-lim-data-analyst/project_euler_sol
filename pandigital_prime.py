# An n-digit number is pandigital if it makes use of all the digits 1 to
# n exactly once. 
# What is the largest n-digit pandigital prime that exists?

from largest_prime_factor import is_prime_number
import itertools

def largest_pandigital_prime():
    """
    Finds the largest n-digit pandigital prime.

    The function generates pandigital numbers by permutation in descending order
    Since it is known that 8- and 9-digit pandigital numbers are divisible by 3,
    checks 7-digit and below.
    """
    # check n-digit pandigital numbers from 7 down to 1.
    for n in range(7, 0, -1):
        # if the sum of digits 1..n is divisible by 3, the number is composite
        digits = ''.join(str(i) for i in range(1, n + 1))
        if sum(map(int, digits)) % 3 == 0:
            continue

        # generate all pandigital numbers (as tuples) in descending order
        for perm in sorted(itertools.permutations(digits), reverse=True):
            num = int(''.join(perm))
            if is_prime_number(num):
                return num
            
    return None

if __name__ == '__main__':
    result = largest_pandigital_prime()
    if result:
        print(f"The largest {len(str(result))}-digit pandigital prime: ", result)
    else:
        print("No pandigital prime found.")