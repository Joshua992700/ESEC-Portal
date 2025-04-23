n = int(input())
m = int(input())
edges = [tuple(map(int,input().split())) for _ in range(m)]
src = int(input())
dest = int(input())

def bfs(edges, src, dest, n):
    adj = {}
    for i,j in edges:
        if i not in adj:
            adj[i] = []
        adj[i].append(j)
    
    vis = [False] * n
    q = [src]
    
    while q:
        node = q.pop(0)
        if node == dest:
            return True
        
        if not vis[node]:
            vis[node] = True
            for x in adj.get(node, []):
                if not vis[x]:
                    q.append(x)
                    
    return False

x = bfs(edges, src, dest, n)
print("YES" if x else "NO")
