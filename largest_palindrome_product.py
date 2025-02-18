# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.
# Find the largest palindrome made from the product of two $3$-digit numbers.

import warnings

def is_palindromic_number(n: int) -> bool:
    """Check if a given number is palindromic.
    
    A palindromic number is a number that remains the same when its digits are reversed.
    
    Args:
        n (int): number to check
    Returns:
        bool: True if n is palidrome, False otherwise
    
    Usage examples:
    >>> is_palindromic_number(464)
    True
    >>> is_palindromic_number(465)
    False"""
    if n < 0:
        raise ValueError("Input parameter cannot be negative")
    
    str_num = str(n)
    return str_num == str_num[::-1]

def find_largest_palindrome(num_digits: int) -> int:
    """Accepts number of digits multiplication and provide the largest
    palindrome product
    Args:
        num_digits (int): n-digits number multiplication
    Returns:
        max palindrome (int)
        
    Usage examples:
    >>> find_largest_palindrome(1)
    9
    >>> find_largest_palindrome(2)
    9009"""
    if num_digits <= 0:
        raise ValueError("input parameter must be positive.")

    if num_digits >= 10:
        warnings.warn(
            "The given number of digits parameter is too high. Risk of numerical overflow.",
            RuntimeWarning
        )
    
    lower_limit = int(10**(num_digits-1))
    upper_limit = int(10**num_digits)
    max_palindrome = None
    for i in range(lower_limit, upper_limit):
        for j in range(i, upper_limit):
            product = i*j
            if is_palindromic_number(product):
                max_palindrome = product

    return max_palindrome

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("The largest palindrome from the product of 2 3-digit numbers:")
    print("-"*10)
    print(find_largest_palindrome(3))