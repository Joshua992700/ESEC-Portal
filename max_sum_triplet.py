def max_sum_triplet(arr):
    n = len(arr)
    max_sum = 0

    # Create an array to store the maximum value to the right of each element
    max_right = [0] * n
    max_right[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], arr[i])

    # Use a set to keep track of the left side elements for the current element
    left_set = set()
    left_set.add(arr[0])
    
    for j in range(1, n - 1):
        if arr[j] < max_right[j + 1]:
            # Find the maximum element smaller than arr[j] in the left_set
            max_left = float('-inf')
            for elem in left_set:
                if elem < arr[j]:
                    max_left = max(max_left, elem)
            if max_left != float('-inf'):
                max_sum = max(max_sum, max_left + arr[j] + max_right[j + 1])
        left_set.add(arr[j])

    return max_sum

# Input handling
n = int(input())
arr = [int(input()) for i in range(n)]
print(max_sum_triplet(arr))
