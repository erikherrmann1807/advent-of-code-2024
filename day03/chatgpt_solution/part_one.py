import re

def sum_valid_mul_instructions_from_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Regular expression to find valid `mul(X,Y)` instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of all valid multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum

# Example usage
file_path = "../input.txt"
result = sum_valid_mul_instructions_from_file(file_path)

# Output the result
print(result)
