# The prime 41, can be written as the sum of 6 consecutive primes:
# 41 = 2 + 3 + 5 +7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime 
# below one hundred.
# Which prime, below one-million, can be written as the sum of the 
# most consecutive primes

from circular_primes import sieve_of_eratosthenes
from largest_prime_factor import is_prime_number

def longest_sum_of_consecutive_primes(limit: int) -> tuple[int, int]:
    """Find the prime below the limit that can be written as the sum
    of the most consecutive primes."""
    primes = sieve_of_eratosthenes(limit)
    max_length = 0
    result_prime = None

    for i in range(len(primes)):
        current_sum = 0
        for j in range(i, len(primes)):
            current_sum += primes[j]
            if current_sum >= limit:
                break

            if is_prime_number(current_sum) and (j - i + 1) > max_length:
                max_length = j - i + 1
                result_prime = current_sum

    return result_prime, max_length

if __name__ == '__main__':
    result_prime, max_length = longest_sum_of_consecutive_primes(1_000_000)
    print("The prime below 1 million that can be written as sum of the \
          most consecutive sum: ", result_prime)
    print("The length of the sequence: ", max_length)