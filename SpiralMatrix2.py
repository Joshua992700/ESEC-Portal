def spiralOrder(matrix):
    result = []
    if not matrix:
        return result
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse downwards
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse upwards
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

def main():
    # Reading input
    M, N = map(int, input().split())
    
    matrix = []
    for _ in range(M):
        row = list(map(int, input().split()))  # Reading a row
        matrix.append(row)  # Append the row to matrix
    
    # Getting spiral order
    result = spiralOrder(matrix)
    
    # Printing the result
    print(" ".join(map(str, result)))

# Example usage
if __name__ == "__main__":
    main()
