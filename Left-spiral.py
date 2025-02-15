# Read matrix dimensions
rows = int(input())
cols = int(input())

# Initialize the matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

top, bottom = 0, rows - 1
left, right = 0, cols - 1  # Corrected indentation here

while top <= bottom and left <= right:
    # Traverse down the leftmost column
    for i in range(top, bottom + 1):
        print(matrix[i][left], end=" ")
    left += 1

    # Traverse across the bottom row
    for i in range(left, right + 1):
        print(matrix[bottom][i], end=" ")
    bottom -= 1

    # Traverse up the rightmost column, if there's anything left
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][right], end=" ")
        right -= 1

    # Traverse across the top row, if there's anything left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[top][i], end=" ")
        top += 1
