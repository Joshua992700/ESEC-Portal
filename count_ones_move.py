def count_ones(n):
    # Initialize an array of size n with all elements as 0
    arr = [0] * n

    # Perform n moves
    for i in range(1, n + 1):
        # Change the element at the position of the multiple of the move number
        for j in range(i - 1, n, i):
            arr[j] = 1 - arr[j]

    # Count the number of 1s in the array
    return sum(arr)

# Example usage
n = int(input())
result = count_ones(n)
print(result)

"""
Input
5

Output
2
"""
