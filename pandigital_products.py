# The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 
# pandigital
# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital

def is_pandigital(n: int) -> bool:
    """Check if a number is 1 to 9 pandigital.
    Args:
        n: int
    Returns:
        boolean, True if a number is pandigital
        
    >>> is_pandigital(985746312)
    True
    >>> is_pandigital(112233778)
    False
    >>> is_pandigital(1)
    False"""
    # convert the number to a string
    str_n = str(n)

    if len(str_n) != 9:
        return False
    
    # check if each digit from 1 to 9 is present exactly once
    for digit in '123456789':
        if str_n.count(digit) != 1:
            return False
        
    return True

def is_unique_digits(n: int) -> bool:
    n_str = str(n)
    return len(set(n_str)) == len(n_str)

def main():
    numbers = []
    for multiplicand in range(2, 100):
        if not is_unique_digits(multiplicand):
            continue
        for multiplier in range(111, 10_000):
            if not is_unique_digits(multiplier):
                continue
            prod = multiplicand * multiplier
            digits = str(multiplicand) + str(multiplier) + str(prod)
            digit_int = int(digits)
            if is_pandigital(digit_int):
                numbers.append(digit_int)
            
    return numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pandigital_numbers = main()

    print(pandigital_numbers)
    print("The sum of all pandigital products: ", sum(pandigital_numbers))