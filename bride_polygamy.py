def find_bride(matrix, n, m):
    sam_position = (0, 0)  # Sam's position (1, 1) in 0-indexed is (0, 0)
    max_qualities = 0
    best_bride = None
    candidates = []

    # Directions for 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(n):
        for j in range(m):
            if (i, j) != sam_position and matrix[i][j] == 1:
                # Count qualities
                qualities = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                        qualities += 1
                
                # Check for the best bride
                if qualities > max_qualities:
                    max_qualities = qualities
                    best_bride = (i + 1, j + 1)  # Store in 1-indexed format
                    candidates = [best_bride]
                elif qualities == max_qualities:
                    candidates.append((i + 1, j + 1))

    if not candidates:
        return "No suitable girl found"
    
    if len(candidates) > 1:
        return "Polygamy not allowed"
    
    return f"{best_bride[0]}:{best_bride[1]}:{max_qualities}"

# Input reading
n, m = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# Find and print the result
result = find_bride(matrix, n, m)
print(result)
