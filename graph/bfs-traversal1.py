n = int(input())
m = int(input())
edges = [tuple(map(int,input().split())) for _ in range(m)]
start = int(input())

adj = {}
for i,j in edges:
    if i not in adj:
        adj[i] = []
    adj[i].append(j)

dp = [False] * n
q = [start]
dp[start] = True
res = []

while q:
    node = q.pop(0)
    res.append(node)
    
    for x in adj.get(node, []):
        if not dp[x]:
            q.append(x)
            dp[x] = True
print(*res)
