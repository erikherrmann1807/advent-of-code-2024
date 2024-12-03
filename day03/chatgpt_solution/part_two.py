import re

def sum_valid_mul_instructions_from_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Regular expressions to find valid instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Track whether mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    # Split the corrupted memory into tokens to process sequentially
    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", corrupted_memory)

    for token in tokens:
        token = token.strip()
        if re.fullmatch(do_pattern, token):
            mul_enabled = True
        elif re.fullmatch(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled and (match := re.fullmatch(mul_pattern, token)):
            x, y = map(int, match.groups())
            total_sum += x * y

    return total_sum

# Example usage
file_path = "../input.txt"
result = sum_valid_mul_instructions_from_file(file_path)

# Output the result
print(result)
