def sort_non_negative(arr):
    # Extract the non-negative numbers and their indices
    non_negatives = [(i, num) for i, num in enumerate(arr) if num >= 0]
    
    # Sort only the non-negative numbers
    sorted_non_negatives = sorted(num for i, num in non_negatives)
    
    # Replace the non-negative numbers in the original array
    j = 0
    for i, num in enumerate(arr):
        if num >= 0:
            arr[i] = sorted_non_negatives[j]
            j += 1
            
    return arr

# Input
n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]

# Sorting the array without changing the position of negative numbers
sorted_arr = sort_non_negative(arr)

# Output
print(" ".join(map(str, sorted_arr)))
