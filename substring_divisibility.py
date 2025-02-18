"""The number, 1406357289 is a 0 to 9 pandigital number because it is 
made up of each of the digits 0 to 9 in some order."""

import itertools

def batched(iterable: list, n: int = 3) -> list:
    """Batch data into lists of certain n length."""
    return [iterable[i:i + n] for i in range(1, len(iterable) - n + 1)]

def main():
    str_digits = '0123456789'
    divisors = [2, 3, 5, 7, 11, 13, 17]
    batched_idxs = batched(list(range(10)))
    # print(batched_idxs)
    numbers_with_prop = set()
    for perm in itertools.permutations(str_digits):
        has_properties = True
        for idxs, divisor in zip(batched_idxs, divisors):
            idx1, idx2, idx3 = idxs
            substring = perm[idx1] + perm[idx2] + perm[idx3]
            num = int(substring)
            if num % divisor != 0:
                has_properties = False
                break

        if has_properties:
            numbers_with_prop.add(int(''.join(perm)))
        
    return numbers_with_prop

if __name__ == '__main__':
    n_with_prop = main()
    print(n_with_prop)
    print("The sum of numbers with the props: ", sum(n_with_prop))