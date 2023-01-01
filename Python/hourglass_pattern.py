
# Hourglass Star Pattern
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
