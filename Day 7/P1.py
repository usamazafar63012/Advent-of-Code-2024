from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate expression left-to-right given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def parse_input(file_path):
    """Parse input data from a file into test values and numbers."""
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                test_value, numbers = line.split(':')
                test_value = int(test_value.strip())
                numbers = list(map(int, numbers.strip().split()))
                equations.append((test_value, numbers))
    return equations

def total_calibration_result(file_path):
    """Calculate the total calibration result for valid equations."""
    equations = parse_input(file_path)
    total = 0
    
    for test_value, numbers in equations:
        num_operators = len(numbers) - 1
        possible_operators = list(product(['+', '*'], repeat=num_operators))
        
        for operators in possible_operators:
            if evaluate_expression(numbers, operators) == test_value:
                total += test_value
                break
    
    return total

# File path to the input file
file_path = "input1.txt"

# Solve and print the result
result = total_calibration_result(file_path)
print("Total Calibration Result:", result)