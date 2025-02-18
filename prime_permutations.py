"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in 2 ways: (i) each of the 3 terms are
prime, and (ii) each of the 4-digit numbers are permutations of one
another. There is one other 4-digit sequence exhibits this property.
What 12-digit number do you form by concatenating the 3 terms in this sequence?"""

import itertools
from largest_prime_factor import is_prime_number

def validate_permutations(list1: list, list2: list) -> bool:
    """Checking if all elements of list1 are in list2 (regardless of
    order).
    Args:
        list1: smaller list
        list2: larger list
    Returns:
        boolean
        
    Usage examples:
    >>> validate_permutations([4, 1], [1, 2])
    False
    >>> validate_permutations(["ace", "bad"], ["cherry", "bad", "ace"])
    True"""
    return all(element in list2 for element in list1) if list1 and list2 \
    else False

def main():
    for i in range(1000, 3340):
        if i == 1487:
            continue

        i2 = i + 3330
        i3 = i2 + 3330
        list_num = [i, i2, i3]
        # check if all numbers are prime
        if not all(is_prime_number(num) for num in list_num):
            continue

        # check for permutations
        str_i = str(i)
        perm = [''.join(p) for p in itertools.permutations(str_i)]
        list_num_str = [str_i, str(i2), str(i3)]

        if validate_permutations(list_num_str, perm):
            return ''.join(list_num_str)
        
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(main())
    