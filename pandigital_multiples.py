# Starting with 9 and multiplying by 1, 2, 3, 4, 5, giving the pandigital,
# 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5)
# what is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2,...,n) where n > 1?

from pandigital_products import is_pandigital, is_unique_digits

def main():
    pandigital_nums = []
    for i in range(1, 10_000):
        if not is_unique_digits:
            continue
        str_number = ''
        for j in range(1, 10):
            if len(str_number) >= 9:
                break
            prod = i * j
            str_number += str(prod)

        number = int(str_number)
        if is_pandigital(number):
            pandigital_nums.append(number)

    return pandigital_nums

if __name__ == '__main__':
    pandigital_numbers = main()

    print(pandigital_numbers)
    print("The largest pandigital 9-digit number: ", max(pandigital_numbers))