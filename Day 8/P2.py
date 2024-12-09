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
    """Calculates unique antinode positions."""
    rows, cols = len(signal_map), len(signal_map[0])
    antinodes = set()
    
    for freq, positions in antennas.items():
        n = len(positions)
        if n < 2:
            continue  # Skip frequencies with only one antenna
            
        # Add all antenna positions (they are antinodes themselves)
        for pos in positions:
            antinodes.add(pos)
        
        # Check for antinodes along lines formed by antennas
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1
                
                # Extend in both directions along the line
                k = 1
                while True:
                    mx, my = x1 - k * dx, y1 - k * dy  # Extend backwards
                    nx, ny = x2 + k * dx, y2 + k * dy  # Extend forwards
                    
                    if 0 <= mx < cols and 0 <= my < rows:
                        antinodes.add((mx, my))
                    if 0 <= nx < cols and 0 <= ny < rows:
                        antinodes.add((nx, ny))
                    
                    # Stop extending when out of bounds
                    if (mx < 0 or mx >= cols or my < 0 or my >= rows) and \
                       (nx < 0 or nx >= cols or ny < 0 or ny >= rows):
                        break
                    k += 1

    return antinodes

def count_unique_antinodes(file_path):
    """Counts the unique antinodes in the signal map."""
    signal_map = read_map(file_path)
    antennas = find_antennas(signal_map)
    antinodes = calculate_antinodes(signal_map, antennas)
    return len(antinodes)

# Example usage
file_path = "input2.txt"  # Replace with the path to your input file
unique_antinodes = count_unique_antinodes(file_path)
print(f"Number of unique antinode locations: {unique_antinodes}")