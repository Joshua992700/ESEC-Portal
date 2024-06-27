def min_time_to_rot_oranges(grid):
    m, n = len(grid), len(grid[0])
    fresh_oranges = 0
    queue = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1
    if not queue and fresh_oranges == 0:
        return "All oranges can become rotten in 0 time frames."
    elif not queue:
        return "All oranges cannot rot"
    time = 0
    while queue:
        time += 1
        size = len(queue)
        for _ in range(size):
            i, j = queue.pop(0)
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh_oranges -= 1
                    queue.append((x, y))
    if fresh_oranges == 0:
        return f"All oranges can become rotten in {time-1} time frames."
    else:
        return "All oranges cannot rot"

m, n = map(int, input().split())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
print(min_time_to_rot_oranges(grid))
