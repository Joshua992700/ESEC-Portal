def is_safe(maze, x, y, N):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 0

def solve_maze_util(maze, x, y, N, solution):
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, N):
        solution[x][y] = 1
        if solve_maze_util(maze, x, y + 1, N, solution) or solve_maze_util(maze, x + 1, y, N, solution):
            return True
        solution[x][y] = 0  # Backtrack
    return False

def solve_maze(maze,N):
    solution = [[0] * N for _ in range(N)]
    if not solve_maze_util(maze, 0, 0, N, solution):
        print("No solution exists")
    else:
        for row in solution:
            print(" ".join(map(str, row)))

N = int(input())
maze = [list(map(int,input().split())) for _ in range(N)]
solve_maze(maze,N)

"""
Input
5
1 0 1 0 1
1 1 1 1 1 
0 0 0 0 0
0 0 0 0 1
1 0 0 0 0
Result 
No solution exists

Input
5
0 0 1 1 1 
1 0 0 1 1
1 1 0 0 1
1 0 1 0 1
1 0 1 0 0
Result
1 1 0 0 0 
0 1 1 0 0 
0 0 1 1 0 
0 0 0 1 0 
0 0 0 1 1 
"""
