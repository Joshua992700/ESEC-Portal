rows = int(input())
cols = int(input())

matrix = [list(map(int,input().split())) for _ in range(rows)]

def solve(x):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    
    def is_valid_rectangle(i1, j1, i2, j2):
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                if matrix[i][j] == 0:
                    return False
        return True

    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    if is_valid_rectangle(i1, j1, i2, j2):
                        max_area = max(max_area, (i2 - i1 + 1) * (j2 - j1 + 1))

    return max_area

print(solve(matrix))
