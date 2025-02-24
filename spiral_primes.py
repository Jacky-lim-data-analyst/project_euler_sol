# starting with 1 and spiralling anticlockwise, 
# a square spiral with side length 7 is formed.
# 8 out of the 13 numbers lying along both diagonals are prime;
# that is a ratio of 8 / 13 $ /approx $ 62%
# If one complete new layer is wrapped around the spiral above, a square
# spiral with side length 9 will be formed. If the process is continued,
# what is the side length of the square spiral for which the ratio of 
# primes along both diagonals first falls below 10%

from largest_prime_factor import is_prime_number

def main():
    current_number = 1
    count_primes = 0
    total_diagonals = 1
    side_length = 1
    increment = 2

    while True:
        # each new spiral layer has 4 corners
        for _ in range(4):
            current_number += increment
            if is_prime_number(current_number):
                count_primes += 1

        total_diagonals += 4
        side_length += 2

        # calculate the ratio of primes on the diagonals
        ratio = count_primes / total_diagonals
        print(ratio)

        if ratio < 0.1:
            break

        # increase the increment for the next layer
        increment += 2

    return side_length

if __name__ == '__main__':
    side_length = main()
    print("The side length: ", side_length)
