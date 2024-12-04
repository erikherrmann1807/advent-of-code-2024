# Solved using chatgpt's help
def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    patterns = [("MAS", "MAS"), ("MAS", "SAM"), ("SAM", "MAS"), ("SAM", "SAM")]
    count = 0

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_x_mas(r, c, diag1, diag2):
        # Check the first diagonal (top-left to bottom-right)
        d1 = [
            (r - 1, c - 1),
            (r, c),
            (r + 1, c + 1)
        ]
        # Check the second diagonal (top-right to bottom-left)
        d2 = [
            (r - 1, c + 1),
            (r, c),
            (r + 1, c - 1)
        ]

        # Validate the diagonals
        for i, (dr, dc) in enumerate(d1):
            if not in_bounds(dr, dc) or grid[dr][dc] != diag1[i]:
                return False
        for i, (dr, dc) in enumerate(d2):
            if not in_bounds(dr, dc) or grid[dr][dc] != diag2[i]:
                return False

        return True

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            for diag1, diag2 in patterns:
                if check_x_mas(r, c, diag1, diag2):
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

    result = count_x_mas(grid)
    print(f"Total occurrences of 'X-MAS': {result}")

if __name__ == "__main__":
    main()
