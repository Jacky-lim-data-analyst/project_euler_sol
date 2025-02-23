# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through a reverse and add process is called a Lychrel number. 
# It is given that for every number below 10_000, it will either become a palindrome in less than fifty iterations, 
# How many Lychrel numbers are there below 10_000?

def is_palindromic_two_digits_n(n: int) -> bool:
    """Check whether a number is a palindrome or not.

    Args:
        n (int): number to check

    Returns:
        bool: True if number is palindrome
    
    Usage example:
    >>> is_palindromic_two_digits_n(11)
    True
    >>> is_palindromic_two_digits_n(9)
    False
    >>> is_palindromic_two_digits_n(568)
    False"""
    if len(str(n)) == 1:
        return False

    n_str = str(n)
    return n_str == n_str[::-1]

def is_lychrel(n: int) -> bool:
    """Is the input n Lychrel number?
    Args:
        n: int
    Returns:
        boolean
    
    Usage examples:
    >>> is_lychrel(196)
    True
    >>> is_lychrel(47)
    False
    >>> is_lychrel(4994)
    True"""
    if n == 0:
        return False

    num_iter = 50
    i = 1
    while i < num_iter:
        num_str = str(n)
        rev_n = int(num_str[::-1])
        n += rev_n
        if is_palindromic_two_digits_n(n):
            return False
        i += 1
        
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    lychrel_set = set()
    for i in range(10_000):
        if is_lychrel(i):
            lychrel_set.add(i)

    print(lychrel_set)
    print("Number of Lychrel numbers below 10,000: ", len(lychrel_set))