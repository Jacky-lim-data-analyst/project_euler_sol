# A permutation is an ordered arrangement of objects. If all of the 
# permutations are listed numerically or alphabetically, we call it 
# lexicographic order.
# what is the millionth lexicographic permutations of the digits 0, 1
# 2, 3, 4, 5, 6, 7, 8, 9
import itertools

digits_str = '0123456789'

print("Calculating...")
for i, n in enumerate(sorted(itertools.permutations(digits_str))):
    if i == 999_999:
        print("The lexicographic permutation is: ")
        print(''.join(n))
        break