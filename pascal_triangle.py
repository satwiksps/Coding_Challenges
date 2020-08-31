
# Pascal's Triangle
def generate_pascals_triangle(rows):
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

rows = 5
triangle = generate_pascals_triangle(rows)
for row in triangle:
    print(" " * (rows - len(row)) + " ".join(map(str, row)))
