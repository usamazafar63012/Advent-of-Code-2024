def read_map(file_path):
    """Reads the antenna map from the file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(signal_map):
    """Identifies all antennas and groups them by frequency."""
    antennas = {}
    for y, row in enumerate(signal_map):
        for x, char in enumerate(row):
            if char.isalnum():  # Check for valid antenna frequency
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(signal_map, antennas):
    """Calculates the unique antinode positions."""
    rows, cols = len(signal_map), len(signal_map[0])
    antinodes = set()
    
    for freq, positions in antennas.items():
        n = len(positions)
        # Compare all pairs of antennas for the same frequency
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Check if x1, y1 is twice the distance from x2, y2
                dx, dy = x2 - x1, y2 - y1
                mx, my = x1 - dx, y1 - dy  # Potential antinode 1
                nx, ny = x2 + dx, y2 + dy  # Potential antinode 2
                
                # Add valid antinodes within bounds
                if 0 <= mx < cols and 0 <= my < rows:
                    antinodes.add((mx, my))
                if 0 <= nx < cols and 0 <= ny < rows:
                    antinodes.add((nx, ny))
    
    return antinodes

def count_unique_antinodes(file_path):
    """Counts the unique antinodes in the signal map."""
    signal_map = read_map(file_path)
    antennas = find_antennas(signal_map)
    antinodes = calculate_antinodes(signal_map, antennas)
    return len(antinodes)

# Example usage
file_path = "input1.txt"  # Replace with the path to your input file
unique_antinodes = count_unique_antinodes(file_path)
print(f"Number of unique antinode locations: {unique_antinodes}")