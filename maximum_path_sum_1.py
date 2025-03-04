# Find the maximum total from top to bottom of the triangle
# This algorithm can solve max path sum 2 too.

def max_path_sum(triangle):
    """Compute the maximum path sum from top to bottom of the given 
    triangle using bottom-up dynamic programming
    
    Args:
        triangle (list of list of int): The number triangle.
        
    Returns:
        int: max path sum"""
    # copy the triangle to avoid modifying the original data
    dp = [row[:] for row in triangle]

    # start from second last row and move upwards
    for row in range(len(dp) - 2, -1, -1):
        for col in range(len(dp[row])):
            # choose the max of 2 possible downward paths
            dp[row][col] += max(dp[row + 1][col], dp[row + 1][col + 1])

    return dp[0][0]

def parse_txt(fn: str) -> list:
    """parse the external text file to a nested list"""
    with open(fn) as f:
        txt_lines = f.readlines()

    nested_lines = []
    for line in txt_lines:
        line = line.strip("\n")
        txt_list = []
        for c in line.split():
            txt_list.append(int(c))

        nested_lines.append(txt_list)

    return nested_lines

if __name__ == '__main__':
    # triangle = [
    #     [75],
    #     [95, 64], 
    #     [17, 47, 82],
    #     [18, 35, 87, 10],
    #     [20, 4, 82, 47, 65],
    #     [19, 1, 23, 75, 3, 34],
    #     [88, 2, 77, 73, 7, 63, 67],
    #     [99, 65, 4, 28, 6, 16, 70, 92],
    #     [41, 41, 26, 56, 83, 40, 80, 70, 33],
    #     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    #     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    #     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    #     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    #     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    #     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    # ]
    filename = "./data/0067_triangle.txt"
    triangle = parse_txt(fn=filename)
    print("maximum path sum: ", max_path_sum(triangle))