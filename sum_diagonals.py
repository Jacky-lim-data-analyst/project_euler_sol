# number spiral diagonals

from enum import Enum

class Direction(Enum):
    SOUTH_EASTERN = 0
    SOUTH_WESTERN = 1
    NORTH_WESTERN = 2
    NORTH_EASTERN = 3

def sum_direction(direction: Direction, n: int) -> int:
    """Sum of numbers in a certain direction"""
    starting_num = 1
    numbers_list = []

    if direction == Direction.SOUTH_EASTERN:
        sum_ = 2

    elif direction == Direction.SOUTH_WESTERN:
        sum_ = 4

    elif direction == Direction.NORTH_WESTERN:
        sum_ = 6
    
    elif direction == Direction.NORTH_EASTERN:
        sum_ = 8

    for _ in range(n):
        next_num = starting_num + sum_
        numbers_list.append(next_num)
        starting_num = next_num
        sum_ += 8

    return sum(numbers_list)

def sum_spiral_diagonals(grid_size: int) -> int:
    """Sum of spiral diagonals given the grid size.
    Args:
        grid_size: int, odd number
    Returns:
        sum of numbers in the diagonal.
    """
    if grid_size < 3:
        raise ValueError("The grid size must be 3 or more.")
    
    if grid_size % 2 == 0:
        raise ValueError("The grid size provided must be odd.")
    
    # sum of different directions
    n = int((grid_size - 1) / 2)
    sum1 = sum_direction(direction=Direction.SOUTH_EASTERN, n=n)
    sum2 = sum_direction(direction=Direction.SOUTH_WESTERN, n=n)
    sum3 = sum_direction(direction=Direction.NORTH_WESTERN, n=n)
    sum4 = sum_direction(direction=Direction.NORTH_EASTERN, n=n)
    
    return sum1 + sum2 + sum3 + sum4 + 1

if __name__ == '__main__':
    print("5x5 grid diagonal spiral sum:")
    print(sum_spiral_diagonals(5))   # 101
    print("3x3 grid diagonal spiral sum:")
    print(sum_spiral_diagonals(3))   # 28
    print("1001x1001 grid diagonal spiral sum:")
    print(sum_spiral_diagonals(1001))   