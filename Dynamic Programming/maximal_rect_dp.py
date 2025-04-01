def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a sentinel value to ensure we can empty the stack at the end.
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

def maxRectangle(matrix):
    if not matrix:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Initialize a height array for each column.
    heights = [0] * m
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'A':
                heights[j] += 1  # Increase height for this column
            else:
                heights[j] = 0  # Reset height if the cell is not 'A'
        
        # Calculate the largest rectangle area for this row (treated as histogram).
        max_area = max(max_area, largestRectangleArea(heights))
    
    return max_area

# Input
n = int(input())
if n == 0:
    print("0")
    exit()

matrix = [input().strip() for _ in range(n)]

# Get the largest rectangle area of 'A's
result = maxRectangle(matrix)
print(result)
