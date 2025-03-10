"""Pentagonal numbers are generated by the formula, $P_n = n(3n-1)/2$.
P_4 + P_7 = 22 + 70 = 92 = P_8, but their difference, 48 is not pentagonal

Find the pair of pentagonal numbers, P_j and P_k, for which their sum
and difference are pentagonal and D = |P_k - P_j| is minimised; 
what is the value of D?"""

def generate_pentagonal_num(n_terms: int) -> list:
    nums = []
    for i in range(1, n_terms + 1):
        # formula
        res = i * (3 * i - 1) // 2
        nums.append(res)

    return nums

def main():
    N = 3000
    pentagonal_nums = generate_pentagonal_num(N)
    pentagonal_set = set(pentagonal_nums)
    min_D = float('inf')  # large number
    num_pair_tuple = None

    for j in range(N - 1):
        for k in range(j + 1, N):
            prev_num = pentagonal_nums[j]
            subsequent_num = pentagonal_nums[k]
            sum_jk = prev_num + subsequent_num
            diff_jk = subsequent_num - prev_num
            if sum_jk in pentagonal_set and diff_jk in pentagonal_set:
                if min_D > diff_jk:
                    min_D = diff_jk
                    num_pair_tuple = (prev_num, subsequent_num)

    return min_D, num_pair_tuple

if __name__ == '__main__':
    min_D, num_pair = main()

    print("The minimum D: ", min_D)
    print("The terms are: ", num_pair)