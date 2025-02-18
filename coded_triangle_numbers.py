# The nth term of the sequence of triangle numbers is given by, t_n =
# n(n+1) / 2.
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# If the word value is a triangle number, then we shall call the word
# a triangle word

import string

def generate_seq_triangle_num(n: int) -> list:
    """Generate sequences of triangle numbers.
    Args:
        n: int, number of terms to generate
    Returns:
        list of triangle numbers
    """
    terms = []
    for i in range(1, n + 1):
        res = int(0.5 * i * (i + 1))
        terms.append(res)

    return terms

def generate_words_order_idx():
    """Generate a dictionary of characters as key and orders as values"""
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chr_order_idx = {}
    for c in characters:
        chr_order_idx[c] = ord(c) - 64
    
    return chr_order_idx

def main():
    # read the text file
    with open("./data/words.txt", "r") as f:
        text = f.read()
    res = text.strip().split(",")
    print(res)
    # generate the sequences of triangle number
    seq_triangle_num = generate_seq_triangle_num(35)
    # print(seq_triangle_num)
    # generate dictionary
    chr_order_dict = generate_words_order_idx()
    # print(chr_order_dict)
    num_triangle_word = 0
    for s in res:
        # remove punctuation from each string
        # string_processed = s.translate(str.maketrans('', '', string.punctuation))
        # print(string_processed)
        # print(s)
        sum_ = 0
        for c in s:
            sum_ += chr_order_dict.get(c.upper(), 0)
        # print(sum_)
        if sum_ in seq_triangle_num:
            num_triangle_word += 1
            print(f"{s} is a triangle word with value of {sum_}")

    return num_triangle_word

if __name__ == '__main__':
    print("Number of triangle word: ", main())