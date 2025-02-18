# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci_sequence_idx(n_digits: int) -> int:
    """Find the index of the first term in the Fibonacci sequence to contain n digits
    Args:
        n_digits: int, number of digits
    Returns:
        int, number of digits
        
    Usage examples:
    >>> fibonacci_sequence_idx(2)
    7
    >>> fibonacci_sequence_idx(3)
    12"""
    fib_seq = [1, 1]
    idx = len(fib_seq)
    while len(str(fib_seq[-1])) < n_digits:
        last_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(last_num)
        idx += 1

    return idx

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("the index of the first term in the Fibonacci sequence to contain 1000 digits")
    print("-"*30)
    print(fibonacci_sequence_idx(4))