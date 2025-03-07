def safe(x,y):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and sol[x][y] == 0
    
def ways(x,y):
    global c
    if (x == 0 and y == n - 1) or (x == n - 1 and y == n - 1) or (x == n - 1 and y == 0) or (x == 0 and y == 0):
        sol[x][y] = 1
        c += 1
        return True
    
    if safe(x,y):
        sol[x][y] = 1
        if ways(x+1,y) or ways(x,y+1) or ways(x-1,y) or ways(x,y-1):
            c += 1
            return True
        sol[x][y] = 0
    return False

n = int(input())
x = int(input())
y = int(input())
c = 0
maze = [list(map(int,input().split())) for _ in range(n)]
sol = [[0]*n for _ in range(n)]

if not ways(x,y):
    print("No solution exists")
else:
    print(f"Minimum Steps: {c}")
    for i in sol:
        print(*i)
