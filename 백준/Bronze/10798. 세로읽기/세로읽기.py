matrix = []

# Read 5 rows of input
for _ in range(5):
    row = list(input().strip())
    matrix.append(row)

# Find the maximum length of the rows
max_length = max(len(row) for row in matrix)

# Output the desired pattern
for col in range(max_length):
    for row in range(5):
        if col < len(matrix[row]):  # Check if the column index is valid for the row
            print(matrix[row][col], end='')
