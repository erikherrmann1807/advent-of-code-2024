def is_safe_report(report):
    # Convert the report string into a list of integers
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check the first condition: all increasing or all decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    # Check the second condition: absolute differences between 1 and 3
    valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

    # The report is safe if both conditions are satisfied
    return (is_increasing or is_decreasing) and valid_differences


def is_safe_with_dampener(report):
    # If the report is already safe, return True
    if is_safe_report(report):
        return True

    # Convert the report string into a list of integers
    levels = list(map(int, report.split()))

    # Test removing each level one by one
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        # Check if the modified report is safe
        if is_safe_report(" ".join(map(str, modified_levels))):
            return True

    # If no single removal makes it safe, return False
    return False


def count_safe_reports_with_dampener(file_path):
    # Open the file and read the lines
    with open(file_path, 'r') as file:
        reports = file.readlines()

    # Count the number of safe reports considering the dampener
    return sum(is_safe_with_dampener(report.strip()) for report in reports)


# Pfad zur Datei
file_path = "../input.txt"  # Ersetze dies durch den tatsächlichen Dateipfad

# Anzahl sicherer Berichte berechnen
safe_count = count_safe_reports_with_dampener(file_path)
print(f"Anzahl der sicheren Berichte mit Dampener: {safe_count}")
