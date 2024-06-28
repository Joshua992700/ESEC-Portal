def read_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            result.append(matrix1[i][j] + matrix2[i][j])
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            result.append(matrix1[i][j] - matrix2[i][j])
    return result

def print_matrix(matrix, operation):
    print(operation + ":")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

# Read dimensions of matrices
rows1, cols1 = map(int, input().split())
rows2, cols2 = map(int, input().split())

if rows1 < 0:
     print("Row and column size should not be negative")
# Check if matrices can be added/subtracted
elif rows1 != rows2 or cols1 != cols2:
    print("Row and column size should be same for 2 matrices")
else:
    # Read matrices
    matrix1 = read_matrix(rows1, cols1)
    matrix2 = read_matrix(rows2, cols2)

    # Add and subtract matrices
    added_matrix = add_matrices(matrix1, matrix2)
    subtracted_matrix = subtract_matrices(matrix1, matrix2)

    print("Addition:")
    for i in added_matrix:
        print(i)

    print("Subtraction:")
    for j in subtracted_matrix:
        print(j)
