def is_safe(x,y):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and sol[x][y] == 0

def backtrack(x,y):
    if x == n - 1 and y == n - 1 and maze[x][y] == 0:
        sol[x][y] = 1
        return True
    
    if is_safe(x,y):
        sol[x][y] = 1
        
        if backtrack(x+1,y) or backtrack(x-1,y) or backtrack(x,y+1) or backtrack(x,y-1):
            return True
        sol[x][y] = 0
    
    return False


n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]

sol = [[0]*n for _ in range(n)] 
if not backtrack(0,0):
    print("No solution exists")
else:
    for i in sol:
        print(*i)
