from collections import defaultdict, deque

def parse_input(file_path):
    """
    Parse the input file into rules and updates.
    """
    with open(file_path, 'r') as f:
        sections = f.read().strip().split("\n\n")
    
    # Parse ordering rules
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
    Check if an update is valid based on the rules.
    """
    required_before = {page: set() for page in update}
    for x, y in rules:
        if x in required_before and y in required_before:
            required_before[y].add(x)

    seen = set()
    for page in update:
        if not required_before[page].issubset(seen):
            return False
        seen.add(page)
    
    return True

def reorder_update(update, rules):
    """
    Reorder an invalid update using the rules to produce a valid sequence.
    """
    # Create a graph for pages in this update
    subgraph = defaultdict(set)
    for x, y in rules:
        if x in update and y in update:
            subgraph[x].add(y)

    # Compute in-degrees
    in_degree = {page: 0 for page in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    # Topological sorting using Kahn's algorithm
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in subgraph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def solve_part_two(file_path):
    """
    Solve Part Two of the problem.
    """
    rules, updates = parse_input(file_path)
    invalid_updates = []

    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)
    
    reordered_updates = [reorder_update(update, rules) for update in invalid_updates]
    middle_sum = sum(update[len(update) // 2] for update in reordered_updates)
    return middle_sum

# File path to the input file
input_file = 'input2.txt'

# Solve Part Two
result = solve_part_two(input_file)
print(f"Sum of middle pages for reordered updates: {result}")