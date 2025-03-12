def safe(x, y):
    return 0 <= x < 8 and 0 <= y < 8 and sol[x][y] == 0
mn=float('inf')
bo=[[float('inf')]*8 for i in range(8)]
def ways(x, y, a, b,c):
    global mn,bo
    if x == a and y == b:
        sol[x][y] = 1
        mn=min(mn,c)
        sol[x][y]=0
        return 
    
    if safe(x, y) and bo[x][y]>c:
        bo[x][y]=c
        sol[x][y] = 1
        # Check all possible knight moves
        if (ways(x + 2, y + 1, a, b,c+1) or 
            ways(x + 1, y + 2, a, b,c+1) or
            ways(x - 1, y + 2, a, b,c+1) or
            ways(x - 2, y + 1, a, b,c+1) or
            ways(x + 1, y - 2, a, b,c+1) or
            ways(x + 2, y - 1, a, b,c+1) or
            ways(x - 1, y - 2, a, b,c+1) or
            ways(x - 2, y - 1, a, b,c+1)):
            return True
        sol[x][y] = 0  # Backtrack
    return False

# Input
x = int(input()) - 1
y = int(input()) - 1
a = int(input()) - 1
b = int(input()) - 1

sol = [[0] * 8 for _ in range(8)]
ways(x,y,a,b,1)

print(mn-1)
