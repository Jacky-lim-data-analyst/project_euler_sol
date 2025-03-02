# The cube, 41063625 (345^3) can be permuted to produce 2 other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the 
# smallest cube which as exactly 3 permutations of its digits which
# are also cube. 
# Find the smallest cube for which exactly five permutations of its
# digits are cube.

from itertools import permutations
from collections import Counter
from factorial_sum_digits import calculate_factorial

def is_cubic_number(n: int) -> bool:
    # compute the cube root of the number
    cube_root = round(n ** (1/ 3))

    return cube_root ** 3 == n
    
def is_num_cubic_permutations(str_num: str, n: int=5) -> bool:
    """determine if exactly n permutations of digits that are cubic"""
    # convert string to a sorted tuple of digits to handle leading zeros
    digit_tuple = tuple(str_num)

    # skip if the number doesn't have enough unique permutations
    digit_counts = Counter(digit_tuple)
    total_possible_permutations = calculate_factorial(len(digit_tuple)) \
    // prod(calculate_factorial(count) for count in digit_counts.values())

    if total_possible_permutations < n:
        return False
    
    # use a set to avoid duplicate permutations
    seen_permutations = set()
    count = 0

    for p in permutations(digit_tuple):
        if p[0] == '0':
            continue

        num = int(''.join(p))

        if num in seen_permutations:
            continue

        seen_permutations.add(num)

        if is_cubic_number(num):
            count += 1

        if count == n:
            return True
        if count + (total_possible_permutations - len(seen_permutations)) < n:
            return False
        
    return False

def prod(iterable):
    """Calculate the product of an iterable."""
    result = 1
    for item in iterable:
        result *= item
    return result

def find_cubic_permutation(start: int=345, limit: int=50_000) -> int:
    """Find the smallest cube for which exactly 5 permutations of its digits"""
    # use a cache for cubic numbers
    cube_cache = set()

    for N in range(start, limit + 1):
        cubic_num = N ** 3

        cube_str = str(cubic_num)
        digit_signature = ''.join(sorted(cube_str))

        if (len(cube_str), digit_signature) in cube_cache:
            continue

        if is_num_cubic_permutations(cube_str):
            return N
        
        cube_cache.add((len(cube_str), digit_signature))

    return None

def main():
    result = find_cubic_permutation()
    print(f"The smallest cube with 5 permutations that are also cubes is: {result}")
    if result:
        cube = result ** 3
        print(f"The cube is: {cube}")

if __name__ == '__main__':
    main()