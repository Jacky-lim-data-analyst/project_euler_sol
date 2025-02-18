# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

def count_Sundays(start_year: int, end_year: int) -> int:
    """Count the number of Sundays on the first of the month from starting year to end year.
    Args:
        start_year: int, starting year
    Returns:
        end_year: int, end year
    
    Usage examples:
    >>> count_Sundays(2025, 2025)
    1"""
    if start_year > end_year:
        raise ValueError("end year must be larger or equal to start year.")
    
    num_Sundays = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            x = datetime.datetime(year, month, 1)
            if x.strftime("%A") == "Sunday":
                num_Sundays += 1

    return num_Sundays

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("Number of Sundays during the 20th century (1 Jan 1901 to 31 Dec 2000)")
    print("-"*10)
    print(count_Sundays(1901, 2000))