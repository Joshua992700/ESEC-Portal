def determinant_2x2(matrix):
    # Formula for 2x2 matrix determinant: ad - bc
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    # Formula for 3x3 matrix determinant:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    
    return (a * (e * i - f * h)) - (b * (d * i - f * g)) + (c * (d * h - e * g))

def main():
    # Read the matrix size
    rows = int(input())  # Number of rows
    cols = int(input())  # Number of columns
    
    # Initialize the matrix
    matrix = []
    
    # Input the matrix elements
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Check if it's a 2x2 or 3x3 matrix and compute the determinant accordingly
    if rows == 2 and cols == 2:
        print(f"Determinant of the matrix ={determinant_2x2(matrix)}")
    elif rows == 3 and cols == 3:
        print(f"Determinant of the matrix ={determinant_3x3(matrix)}")
    else:
        print("This program only supports 2x2 and 3x3 matrices.")

# Example usage
if __name__ == "__main__":
    main()


"""
Input
2
2
1 2
3 4

Output
Determinant of the matrix =-2
"""
