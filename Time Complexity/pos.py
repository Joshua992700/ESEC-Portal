def find_min_sum_of_factors(N):
    min_sum = float('inf')  # Initialize with a large value
    # Iterate over possible factors from 1 to sqrt(N)
    for A in range(1, int(N ** 0.5) + 1):
        if N % A == 0:  # If A is a factor
            B = N // A  # The corresponding B
            min_sum = min(min_sum, A + B)  # Update the minimum sum
    return min_sum

# Input
N = int(input())

# Output the result
print(find_min_sum_of_factors(N))
