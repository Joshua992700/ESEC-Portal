m = []
try:
    for i in range(10):
        m.append(list(map(int,input().split())))
except:
    pass

def solve(x):
    if not x:
        return 0
    
    n = len(x)
    m = len(x[0])
    dp = [[0] * n for _ in range(m)]
    
    def dfs(i,j):
        if dp[i][j] != 0:
            return dp[i][j]
        
        l = 1
        if j + 1 < m and x[i][j+1] == x[i][j]+1:
            l = max(l,dfs(i,j + 1) + 1)
        if j - 1 < m and x[i][j-1] == x[i][j]+1:
            l = max(l,dfs(i,j - 1) + 1)
        if i + 1 < n and x[i+1][j] == x[i][j]+1:
            l = max(l,dfs(i + 1,j) + 1)
        if j - 1 < m and x[i-1][j] == x[i][j]+1:
            l = max(l,dfs(i - 1,j) + 1)
        
        return l
    
    p = 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0:
                p = max(p,dfs(i,j))
    return p

print(solve(m))
