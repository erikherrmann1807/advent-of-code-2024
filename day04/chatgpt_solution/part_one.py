def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not in_bounds(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1
    return count

# Main function to read input from a file
def main():
    file_path = input("Enter the path to the text file containing the word search: ").strip()

    try:
        with open(file_path, "r") as file:
            grid = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return

    if not grid:
        print("The file is empty or contains no valid rows!")
        return

    result = count_xmas(grid)
    print(f"Total occurrences of 'XMAS': {result}")

if __name__ == "__main__":
    main()
