# quadratic primes

def is_prime_number(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    max_primes = 0
    best_a = 0
    best_b = 0

    for a in range(1, 50):
        for b in range(1, 50):
            n = 0
            while True:
                value = n * n + a * n + b
                if value >= 2:
                    if not is_prime_number(value):
                        break
                    n += 1
            if n > max_primes:
                max_primes = n
                best_a = a
                best_b = b

    print(f"The maximum number of consecutive primes is {max_primes}")
    print(f"The values of a and b are {best_a} and {best_b} respectively.")
    print(f"a * b = {best_a * best_b}")

if __name__ == '__main__':
    main()