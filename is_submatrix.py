def is_submatrix(big_matrix, small_matrix, N, M):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            match = True
            for k in range(M):
                for l in range(M):
                    if big_matrix[i + k][j + l] != small_matrix[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    
    # Read the size of the larger matrix
    N = int(data[idx])
    idx += 1
    
    # Read the larger matrix
    big_matrix = []
    for i in range(N):
        row = list(map(int, data[idx:idx + N]))
        big_matrix.append(row)
        idx += N
    
    # Read the size of the smaller matrix
    M = int(data[idx])
    idx += 1
    
    # Read the smaller matrix
    small_matrix = []
    for i in range(M):
        row = list(map(int, data[idx:idx + M]))
        small_matrix.append(row)
        idx += M
    
    # Check if the smaller matrix is a submatrix of the larger matrix
    if is_submatrix(big_matrix, small_matrix, N, M):
        print("True")
    else:
        print("False")

# Example usage
main()
