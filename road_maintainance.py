def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def solve():
    m = []
    try:
        while True:
            x, y, w = map(int, input().split())
            m.append([x-1, y-1, w])
    except:
        pass
    
    m.sort(key=lambda edge: edge[2])

    N = max(max(x, y) for x, y, _ in m) + 1
    p = list(range(N))
    ans = 0
    edge_count = 0

    for x, y, w in m:
        pa = find(x)
        pb = find(y)
        
        if pa != pb:
            p[pa] = pb
            ans += w
            edge_count += 1

        if edge_count == N - 1:
            break

    if edge_count != N - 1:
        print(-1)
    else:
        print(ans)

solve()
