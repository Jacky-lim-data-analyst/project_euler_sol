# The number, 197 is called a circular prime because all rotations of
# the digits: 197, 971, 719

# Use sieve of eratosthenes to find prime numbers up to one million

def sieve_of_eratosthenes(limit: int) -> list:
    is_prime = [True] * (limit + 1)
    p = 2

    while (p * p <= limit):
        if is_prime[p] == True:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

        p += 1
    
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers

def is_prime(n: int, primes_set: set) -> bool:
    return n in primes_set

def generate_rotations(n: int):
    str_n = str(n)
    rotations = [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]
    return rotations

def count_circular_primes(limit: int) -> int:
    primes = sieve_of_eratosthenes(limit)
    primes_set = set(primes)
    circular_primes_count = 0

    for prime in primes:
        rotations = generate_rotations(prime)
        if all(is_prime(rotation, primes_set) for rotation in rotations):
            circular_primes_count += 1

    return circular_primes_count

if __name__ == '__main__':
    limit = 1_000_000

    circular_primes_count = count_circular_primes(limit)

    print("The number of circular primes below 1 million: ", circular_primes_count)