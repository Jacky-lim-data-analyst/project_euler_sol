# find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def is_sum_of_fifth_powers(n: int) -> bool:
    digits = [int(i) for i in str(n)]
    fifth_powers_sum = sum(i ** 5 for i in digits)
    return fifth_powers_sum == n

def find_numbers_with_fifth_power_sum() -> list:
    results = []
    for num in range(2, 1_000_000):     # assuming the range is reasonable
        if is_sum_of_fifth_powers(num):
            results.append(num)

    return results

if __name__ == '__main__':
    res = find_numbers_with_fifth_power_sum()
    print(res)
    print("The sum of the numbers: ", sum(res))