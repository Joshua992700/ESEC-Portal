def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    height = [0] * cols  # This will store the height of the histogram bars
    max_area = 0

    # Helper function to calculate the largest rectangle area in a histogram
    def max_hist_area(heights):
        stack = []
        max_area_hist = 0
        index = 0

        while index < len(heights):
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                max_area_hist = max(max_area_hist, area)

        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area_hist = max(max_area_hist, area)

        return max_area_hist

    # Traverse through the matrix row by row
    for row in matrix:
        for i in range(cols):
            if row[i] == "1":
                height[i] += 1  # Increase the height of the histogram bar
            else:
                height[i] = 0  # Reset height if it's '0'

        # Calculate the maximum area for the current histogram
        max_area = max(max_area, max_hist_area(height))

    return max_area

# Example input
m = int(input())
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(m)]

# Call the function
print(maximalRectangle(matrix))
