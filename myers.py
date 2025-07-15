def min_total_marks(n, marks):
    marks.sort()
    total = marks[0]
    prev = marks[0]
    
    for i in range(1, n):
        if marks[i] > prev:
            total += marks[i]
            prev = marks[i]
        else:
            prev += 1
            total += prev
            
    return total

# Read input
n = int(input())
marks = [int(input()) for _ in range(n)]

# Compute result
print(min_total_marks(n, marks))
