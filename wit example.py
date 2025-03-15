
with open("example.txt", "r") as file:
    lines = file.readlines()
    # Count the number of lines
    line_count = len(lines)

print(f"The file contains {line_count} lines.")
