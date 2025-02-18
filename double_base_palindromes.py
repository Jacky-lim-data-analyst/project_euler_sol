# the decimal number, 585 = 1001001001_2 (binary), is palindromic in both
# bases. Find the sum of all numbers, less than 1_000_000, which are
# palindromic in base 10 and base 2.

def is_palindromic(n: str) -> bool:
    return n[::-1] == n

def is_palindromic_double_base(n: int) -> bool:
    """Checks is n is palindrome in both 10 and 2 bases.
    Args:
        n: int
    Returns:
        boolean, True if palindromic in both bases
    
    >>> is_palindromic_double_base(585)
    True
    >>> is_palindromic_double_base(9)
    True
    >>> is_palindromic_double_base(50)
    False"""
    num_2_base = bin(n)
    num_2_base = num_2_base[2:]
    num_str = str(n)
    return is_palindromic(num_2_base) and is_palindromic(num_str)
    
def main():
    palindromes_double_bases = []
    for i in range(1, 1_000_000):
        if is_palindromic_double_base(i):
            palindromes_double_bases.append(i)

    return palindromes_double_bases

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    palindromes_double_bases = main()

    print(palindromes_double_bases)
    print("The sum of double-base palindromes under 1 million: ", \
          sum(palindromes_double_bases))