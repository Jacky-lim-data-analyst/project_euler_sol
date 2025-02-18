# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 inclusive were written out in words,
# how many letters would be used?
num_words_dict = {
    # "0": 4,
    "1": 3,
    "2": 2,
    "3": 5,
    "4": 4,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 5,
    "9": 4,
    "10": 3,
    "11": 6,
    "12": 6,
    "13": 8,
    "14": 8,
    "15": 7,
    "16": 7,
    "17": 9,
    "18": 8,
    "19": 8,
    "20": 6,
    "30": 6,
    "40": 6,
    "50": 5,
    "60": 5,
    "70": 7,
    "80": 6,
    "90": 6,
    # "100": 7,
    # "1000": 8
}

def handle_two_digit_num(n_str: str) -> int:
    if n_str.endswith("0"):
        num_letters = num_words_dict[n_str]
    else:
        if n_str.startswith("1"):
            num_letters = num_words_dict[n_str]

        else:
            key = n_str[0] + "0"
            num_letters = num_words_dict[key] + num_words_dict[n_str[1]]
        
    return num_letters

def count_letters(n_str: str) -> int:
    """Count letters of numbers
    Args:
        n_str: string, number string
    Returns:
        int, number of English letters
        
    Usage examples:
    >>> count_letters("5")
    4
    >>> count_letters("27")
    11
    >>> count_letters("318")
    23
    >>> count_letters("409")
    18"""
    if len(n_str) == 1:
        num_letters = num_words_dict[n_str]
    elif len(n_str) == 2:
        num_letters = handle_two_digit_num(n_str)

    elif len(n_str) == 3:
        num_letters = num_words_dict[n_str[0]] + 10
        if n_str[1] != "0":
            num_letters += handle_two_digit_num(n_str[1:])
        else:
            if n_str[2] == "0":
                num_letters -= 3
            else:
                num_letters += num_words_dict[n_str[2]]
        
    if int(n_str) == 1000:
        num_letters = 11

    return num_letters

def main():
    num_letters = 0
    for i in range(1, 1001):
        num_str = str(i)
        # print(i)
        num_letters += count_letters(num_str)

    return num_letters

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("The number of letters used: ", main())