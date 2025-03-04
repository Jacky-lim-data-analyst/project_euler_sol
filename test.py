# from itertools import permutations

# print(list(permutations('abcd')))
# print(sum([True, True, False, False, False]))

# print(tuple('abcde'))

# def continued_fraction_sqrt(n, terms=10):
#     """
#     Compute the continued fraction representation of the square root of n.

#     Args:
#         n: A positive integer whose square root we want to represent as continued fraction
#         terms: The number of terms to compute in the continued fraction expansion

#     Returns:
#         A list where the first element is the integer part and
#         the remaining form the repeating part of the continued fraction
#     """
#     if n <= 0:
#         raise ValueError("Input must be a positive integer")
    
#     # check if n is a perfect square
#     sqrt_n = int(n**0.5)
#     if sqrt_n * sqrt_n == n:
#         return [sqrt_n]
    
#     # initialize variables for the continued fraction algorithm
#     a0 = sqrt_n
#     m = 0
#     d = 1
#     a = a0

#     # List to store the terms of the continued fraction
#     cf_terms = [a0]

#     # detect the period
#     seen_states = {}

#     for i in range(terms):
#         m = d * a - m
#         d = (n - m * m) // d
#         a = (a0 + m) // d

#         # store the current state
#         state = (m, d, a)

#         if state in seen_states:
#             period_start = seen_states[state]

#             return cf_terms[:period_start] + cf_terms[period_start:]
        
#         seen_states[state] = len(cf_terms)
#         cf_terms.append(a)

#     return cf_terms

# if __name__ == '__main__':
#     result = continued_fraction_sqrt(7)
#     print(result)

with open("./data/0067_triangle.txt") as f:
    txt_lines = f.readlines()

print(type(txt_lines))
print(len(txt_lines))
print(txt_lines[:10])

nested_lines = []
for line in txt_lines[:10]:
    line = line.strip("\n")
    txt_list = []
    for c in line.split():
        txt_list.append(int(c))

    nested_lines.append(txt_list)

print(nested_lines)