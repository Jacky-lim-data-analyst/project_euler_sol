# The sequence of triangle number is generated by adding the natural numbers. 
# The 7th triangle number would be 1 + 2 + ... + 7 = 28. 
# The first 10 terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# List down the factors (divisors) of the first 4 triangle numbers:
# 1: 1; 3: 1, 3; 6: 1, 2, 3, 6; 10: 1, 2, 5, 10

def generate_triangle_number(n: int) -> int:
    """Output triangle number.
    Args:
        n: int, the nth term.
    Returns:
        int: triangle number
        
    Usage examples:
    >>> generate_triangle_number(2)
    3
    >>> generate_triangle_number(7)
    28
    >>> generate_triangle_number(10)
    55"""
    if n <= 0:
        raise ValueError("The input parameter cannot be zero or negative.")
    
    return int((n * (1 + n)) * 0.5)

def find_num_divisors(triangle_num: int) -> int:
    """Find the number of divisors of triangle number.
    Args:
        triangle_num: int, triangle number.
    Returns:
        int: number of factors / divisors
    
    Usage examples:
    >>> find_num_divisors(10)
    4
    >>> find_num_divisors(36)
    9"""
    if triangle_num <= 0:
        raise ValueError("The input parameter cannot be zero or negative.")
    
    return len([i for i in range(1, triangle_num + 1) if triangle_num % i == 0])

def main():
    required_num_divisors = input("What is the first triangle number to have nth divisiors? ")
    
    try:
        # Attempt to convert the input to an integer
        rnd = int(required_num_divisors)
        print(f"The first triangle number to reach {rnd} divisors: ")
    except ValueError:
        print("The input is not an integer.")
        return 

    num_divisors = 0
    count = 0
    triangle_number = 0
    # first triangle number to have over 500 divisors
    while num_divisors < rnd:
        count += 1
        triangle_number = generate_triangle_number(count)
        num_divisors = find_num_divisors(triangle_number)

    print(triangle_number)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()