def parse_input(file_path):
    """
    Parse the input file into rules and updates.
    """
    with open(file_path, 'r') as f:
        sections = f.read().strip().split("\n\n")
    
    # Parse rules
    rules = []
    for line in sections[0].splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    # Parse updates
    updates = []
    for line in sections[1].splitlines():
        updates.append(list(map(int, line.split(','))))
    
    return rules, updates


def is_valid_update(update, rules):
    """
    Check if an update sequence is valid based on the given rules.
    """
    # Create a mapping of each page to its required predecessors
    required_before = {page: set() for page in update}
    for x, y in rules:
        if x in required_before and y in required_before:
            required_before[y].add(x)

    # Validate the update order
    seen = set()
    for page in update:
        # All required predecessors must have been seen before this page
        if not required_before[page].issubset(seen):
            return False
        seen.add(page)
    
    return True


def solve(file_path):
    """
    Solve the problem and return the sum of middle pages for valid updates.
    """
    rules, updates = parse_input(file_path)
    valid_middle_sum = 0
    
    for update in updates:
        if is_valid_update(update, rules):
            middle_index = len(update) // 2
            valid_middle_sum += update[middle_index]
    
    return valid_middle_sum


# File path to the input file
input_file = 'input1.txt'

# Solve the problem
result = solve(input_file)
print(f"Sum of middle pages for valid updates: {result}")