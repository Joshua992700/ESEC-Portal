rows = int(input())
cols = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

def solve(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    
    def is_valid_rectangle(x, y, a, b):
        for i in range(x, a + 1):
            for j in range(y, b + 1):
                if matrix[i][j] == 0:
                    return False
        return True

    for x in range(rows):
        for y in range(cols):
            for a in range(x, rows):
                for b in range(y, cols):
                    if is_valid_rectangle(x, y, a, b):
                        max_area = max(max_area, (a - x + 1) * (b - y + 1))

    return max_area

print(solve(matrix))
