# Christian Goldbach proposed that every odd composite number can be 
# written as the sum of a prime and twice a square
# It turns out the conjecture was false.
# What is the smallest odd composite that cannot be written as the
# sum of a prime and twice a square?

def is_prime_number(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def is_composite(n: int) -> bool:
    """Check if a number is composite."""
    if n < 4:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    
    return False

def generate_odd_composite_num(upper_limit: int) -> set:
    """Generate odd composite numbers up to the upper limit."""
    nums = set()
    for i in range(3, upper_limit, 2):
        if is_composite(i):
            nums.add(i)

    return nums

def main():
    """find the smallest odd composite that violate the conjecture"""
    # generate odd composite numbers
    odd_composites = generate_odd_composite_num(1_000_000)
    # print(odd_composites)

    for odd_composite in odd_composites:
        violation_flag = True
        for i in range(1, 709):
            current_res = odd_composite - 2 * i * i

            if is_prime_number(current_res):
                violation_flag = False
                break
        
        if violation_flag:
            return odd_composite

if __name__ == '__main__':
    smallest_odd_composite = main()
    print("The smallest odd composite that violate the conjecture: ", \
          smallest_odd_composite)