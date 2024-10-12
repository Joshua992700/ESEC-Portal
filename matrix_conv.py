def rotate(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Read input
s = input()
matrix2 = eval(s)

# Rotate the matrix
rotate(matrix2)

# Format and print the matrix
output = "[" + ",".join("[" + ",".join(map(str, row)) + "]" for row in matrix2) + "]"
print(output)

"""
Input
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Result
[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
