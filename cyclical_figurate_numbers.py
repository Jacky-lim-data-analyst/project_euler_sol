# find the sum of the only ordered set of six cyclic 4-digit numbers 
# for which each polygonal type: triangle, square, pentagonal, 
# hexagonal, heptagonal, heptagonal and octagonal is represented by a different
# number in the set

def generate_figurate_numbers(s, digits=4):
    """Generate s-gonal numbers with the specified number of digits."""
    results = []
    n = 1

    while True:
        if s == 3:      # triangular
            num = n * (n + 1) // 2
        elif s == 4:    # square
            num = n ** 2
        elif s == 5:    # pentagonal
            num = n * (3 * n - 1) // 2
        elif s == 6:
            num = n * (2 * n - 1)
        elif s == 7:
            num = n * (5 * n - 3) // 2
        elif s == 8:
            num = n * (3 * n - 2)
        else:
            raise ValueError(f"invalid polygonal type: {s}")
        
        if num >= 10**(digits - 1) and num < 10**digits:
            results.append(num)
        elif num >= 10**digits:
            break

        n += 1

    return results

def is_cyclic(nums):
    """Check if the list of numbers is cyclic."""
    for i in range(len(nums)):
        last_two_digits = nums[i] % 100
        first_two_digits = nums[(i+1) % len(nums)] // 100

        if last_two_digits != first_two_digits:
            return False
        
    return True

def find_cyclic_figurate_set():
    # Generate all figurate numbers for each type
    figurate_numbers = {}
    for s in range(3, 9):  # 3 to 8 for different polygonal types
        figurate_numbers[s] = generate_figurate_numbers(s)
    
    # Create a mapping to quickly check if a number is of a specific figurate type
    figurate_type_map = {}
    for s, nums in figurate_numbers.items():
        for num in nums:
            if num not in figurate_type_map:
                figurate_type_map[num] = []
            figurate_type_map[num].append(s)
    
    # Find potential starting numbers (we'll use octagonal as the starting point)
    for start_num in figurate_numbers[8]:  # Start with octagonal numbers
        # Initialize path with the starting number
        path = [start_num]
        used_types = [8]  # We've used an octagonal number
        
        # Find cyclic sequences
        find_cyclic_sequence(path, used_types, figurate_type_map)
        
        # Check if we found a solution
        if len(found_solution) == 6:
            return found_solution

# Global variable to store the solution
found_solution = []

def find_cyclic_sequence(path, used_types, figurate_type_map):
    global found_solution
    
    # If we already found a solution, return
    if len(found_solution) == 6:
        return
    
    # If we've used all 6 types and the sequence is cyclic
    if len(path) == 6:
        if is_cyclic(path):
            found_solution = path.copy()
        return
    
    # Get the last number's last two digits
    last_two = path[-1] % 100
    
    # Find potential next numbers
    for next_num, types in figurate_type_map.items():
        # Next number must start with last_two
        if next_num // 100 == last_two:
            # Check if there's an unused figurate type for this number
            for type_num in types:
                if type_num not in used_types:
                    # Add this number and type to our path
                    path.append(next_num)
                    used_types.append(type_num)
                    
                    # Recursively find next numbers
                    find_cyclic_sequence(path, used_types, figurate_type_map)
                    
                    # If we found a solution, return
                    if len(found_solution) == 6:
                        return
                    
                    # Backtrack
                    path.pop()
                    used_types.pop()

def main():
    solution = find_cyclic_figurate_set()
    print("Cyclic set of figurate numbers:", solution)
    print("Sum:", sum(solution))
    
    # Verify that each number in the set is of a different figurate type
    for s in range(3, 9):
        figurate_set = set(generate_figurate_numbers(s))
        for num in solution:
            if num in figurate_set:
                print(f"{num} is a {s}-gonal number")
                break

if __name__ == "__main__":
    main()