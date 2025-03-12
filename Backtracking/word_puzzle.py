maze=[['A','B','C','I'],['B','I','C','S'],['C','D','E','E']]

def bt(maze,word):  
    rows = len(maze)
    cols = len(maze[0])
    path = set()
    
    def solve(r,c,i):
        if i == len(word):
            return True
        
        if 0 > r or r >= rows or 0 > c or c >= cols or word[i] != maze[r][c] or (r,c) in path:
            return False
        path.add((r,c))
        res = solve(r+1,c,i+1) or solve(r-1,c,i+1) or solve(r,c+1,i+1) or solve(r,c-1,i+1)
        path.remove((r,c))
        return res
    
    for i in range(rows):
        for j in range(cols):
            if solve(i,j,0):
                return True
    return False
    
for i in range(int(input())):
    print(bt(maze,input()))
