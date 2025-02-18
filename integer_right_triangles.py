# if p is the perimeter of a right angle triangle with integral length
# sides, {a, b, c}, there are exactly 3 solutions for p = 120.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# for which value of p <= 1000, is the number of solutions maximised?

from collections import defaultdict
import math

def main():
    dd = defaultdict(int)
    for a in range(1, 500):
        for b in range(1, 500):
            c_squared = a ** 2 + b ** 2
            c = math.isqrt(c_squared)
            if c * c == c_squared:
                sum_ = a + b + c
                if sum_ <= 1000:
                    dd[sum_] += 1

    return dd

if __name__ == '__main__':
    data = main()

    print("The value p with maximum number of Pythagorean triplets: ", max(data, key=data.get))