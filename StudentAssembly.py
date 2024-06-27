def count_misplaced_students(heights):
    sorted_heights = sorted(heights)
    misplaced = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            misplaced += 1
    return misplaced

n = int(input())
heights = list(map(int, input().split()))
print(count_misplaced_students(heights))
