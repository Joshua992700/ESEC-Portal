def longestIncreasingPath(x):
    if not x:
        return 0

    n = len(x)
    m = len(x[0])
    dp = [[0] * m for _ in range(n)]

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]

        max_length = 1

        if j + 1 < m and x[i][j + 1] == x[i][j] + 1:
            max_length = max(max_length, 1 + dfs(i, j + 1))

        if i + 1 < n and x[i + 1][j] == x[i][j] + 1:
            max_length = max(max_length, 1 + dfs(i + 1, j))

        return max_length

    max_path = 0

    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0:
                max_path = max(max_path, dfs(i, j))

    return max_path

m = []
try:
    for i in range(10):
        m.append(list(map(int, input().split(','))))
except:
    pass

print(longestIncreasingPath(m))
