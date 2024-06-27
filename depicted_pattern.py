n = int(input())
size = 2 * n - 1

pattern = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        pattern[i][j] = n - min(min(i, j), min(size - 1 - i, size - 1 - j))

for row in pattern:
    print(" ".join(map(str, row)))
