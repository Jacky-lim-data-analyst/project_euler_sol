# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 
# 20 x 20 grid?
import numpy as np
from enum import Enum

grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

class Direction(Enum):
    UP_DOWN = 0
    LEFT_RIGHT = 1
    DIAGONAL = 2

# Strip the grid to remove any white spaces and split by line break
lines = grid.strip().splitlines()

# convert to list of integers
grid_list = [list(map(int, line.split())) for line in lines]

# convert to Numpy array
arr = np.array(grid_list)

# find greatest product 
def find_greatest_prod(n: int, direction: Direction) -> int:
    """Find the greatest product of n consecutive integers 
    in chosen direction.
    Args:
        n: int, number of adjacent integer multiplied.
        direction: enum, UP_DOWN=0, LEFT_RIGHT=1, DIAGONAL=2
    
    Returns:
        int, product of multiplication of n consecutive numbers
        
    Usage examples:
    >>> find_greatest_prod(4, Direction.DIAGONAL)
    np.int64(32719995)"""
    if n <= 1:
        raise ValueError("Number of adjacent integer should more than or \
                         equal to 2")
    
    if n > 20:
        raise ValueError("n exceeded the height or width of grid")

    row, col = arr.shape
    greatest_prod = 0
    if direction == Direction.UP_DOWN:
        for j in range(col):
            for i in range(row - n):
                numbers = arr[i:i+n, j]
                prod = np.prod(numbers)
                if prod > greatest_prod:
                    greatest_prod = prod

    if direction == Direction.LEFT_RIGHT:
        for i in range(row):
            for j in range(col - n):
                numbers = arr[i, j:j+n]
                prod = np.prod(numbers)
                if prod > greatest_prod:
                    greatest_prod = prod

    if direction == Direction.DIAGONAL:
        for i in range(row - n):
            for j in range(col - n):
                numbers = arr[np.arange(i, i + n), np.arange(j, j + n)]
                prod = np.prod(numbers)
                if prod > greatest_prod:
                    greatest_prod = prod

    return greatest_prod

def find_products(n: int, direction: Direction, **starting_pos) -> int:
    """Find products of n consecutive numbers in a grid
    Args:
        n: int, number of consecutive numbers
        direction: enum
        **kwargs: dict, starting position with keys: row and column
        
    Returns:
        product of the specified numbers
        
    Usage examples:
    >>> find_products(2, Direction.LEFT_RIGHT, row=0, col=0)
    np.int64(16)
    >>> find_products(3, Direction.UP_DOWN, row=17, col=0)
    np.int64(400)
    >>> find_products(2, Direction.DIAGONAL, row=18, col=14)
    np.int64(81)""" 
    x = starting_pos["row"]
    y = starting_pos["col"]
    row, col = arr.shape

    if n <= 1:
        raise ValueError("Number of adjacent integer should more than or \
                         equal to 2")
    
    if n > 20:
        raise ValueError("n exceeded the height or width of grid")
    
    if direction == Direction.DIAGONAL:
        if (x + n > row) or (y + n > col):
            raise IndexError("Out of bound (diagonal)")
        numbers = arr[np.arange(x, x+n), np.arange(y, y+n)]
        
    if direction == Direction.LEFT_RIGHT:
        if y + n > col:
            raise IndexError("Out of bound (horizontal)")
        numbers = arr[x, np.arange(y, y+n)]
    
    if direction == Direction.UP_DOWN:
        if x + n > row:
            raise IndexError("Out of bound (vertical)")
        numbers = arr[np.arange(x, x+n), y]
        
    return np.prod(numbers)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Marked in red: ", find_products(4, Direction.DIAGONAL, row=6, col=8))