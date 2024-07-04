def is_sparse_matrix(m, n, matrix):
    zero_count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_count += 1
    if zero_count >= (m * n) / 2:
        return True
    else:
        return False

m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_sparse_matrix(m, n, matrix):
    print("The given matrix is Sparse matrix")
else:
    print("The given matrix is not a Sparse matrix")
