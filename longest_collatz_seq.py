# The following iterative sequence is defined for the set of positive integers:
# n -> n / 2 (n even)
# n -> 3n + 1 (n odd)

def count_num_terms(starting_num: int) -> int:
    """Count number of terms in Collatz sequence from the starting number.
    Args:
        starting num: int
    
    Returns:
        int, number of terms in the Collatz sequence
        
    Usage examples:
    >>> count_num_terms(2)
    2
    >>> count_num_terms(13)
    10"""
    if starting_num <= 1:
        raise ValueError("The starting number must be more than 1.")
    
    collatz_seq = [starting_num]
    end_num = starting_num
    while end_num != 1:
        if end_num % 2 == 0:
            end_num /= 2
        else:
            end_num = 3 * end_num + 1
        collatz_seq.append(end_num)

    return len(collatz_seq)

def main():
    upper_limit = 1_000_000
    len_seq_max = 0
    starting_num_max = 0
    for start_num in range(2, upper_limit):
        num_terms = count_num_terms(start_num)
        if len_seq_max < num_terms:
            len_seq_max = num_terms
            starting_num_max = start_num

    print(f"The starting number {starting_num_max} produces the longest chain, which is \n")
    print(len_seq_max)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()