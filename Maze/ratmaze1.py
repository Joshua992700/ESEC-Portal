def is_safe(maze,x,y,n):
    return 0<=x<n and 0<=y<n and maze[x][y] == 0
    
def solve(maze,x,y,n,sol):
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        return True
    
    if is_safe(maze,x,y,n):
        sol[x][y] = 1
        if solve(maze,x+1,y,n,sol) or solve(maze,x,y+1,n,sol):
            return True
        sol[x][y] = 0
    return False

n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]

x = [[0]*n for _ in range(n)]
if not solve(m,0,0,n,x):
    print("No solution exists")
else:
    for i in x:
        print(*i)
