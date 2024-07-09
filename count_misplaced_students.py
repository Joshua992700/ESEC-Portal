def count_misplaced_students(heights):
    
    sorted_heights = sorted(heights)
    misplaced_count = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            misplaced_count += 1
    return misplaced_count

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Count and print the number of misplaced students
print(count_misplaced_students(heights))
