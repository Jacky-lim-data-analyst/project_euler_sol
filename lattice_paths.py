# use dynamic programming approach to count the number of unique paths
# from one point to another on a lattice grid. Can be implemented using
# a 2D list (array) to store the number of ways to reach each point on the grid

from typing import Union

def count_unique_paths(grid_size: Union[tuple, list]) -> int:
    """Count the number of unique paths
    Args:
        grid_size: tuple or list with 2 entries (height x width)
    Returns:
        int, number of unique paths
        
    Usage examples:
    >>> count_unique_paths((2, 3))
    3
    >>> count_unique_paths((3, 3))
    6"""
    rows, cols = grid_size

    # initialize a 2D list to store the number o unique paths to each point
    dp = [[0] * cols for _ in range(rows)]

    # There is exactly one way to be at the starting point
    dp[0][0] = 1

    # Fill the first row and first column
    for i in range(1, rows):
        dp[i][0] = 1
    for j in range(1, cols):
        dp[0][j] = 1

    # fill the rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # the bottom-right corner will have the total number of unique paths
    return dp[rows-1][cols-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("The number of routes through 20x20 grid: ", count_unique_paths((21, 21)))