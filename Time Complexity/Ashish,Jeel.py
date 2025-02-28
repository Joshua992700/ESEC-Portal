T = int(input())  # Number of test cases
    
for _ in range(T):
    N = int(input())  # Size of the array
    A = list(map(int, input().split()))  # The array
    
    # Precompute max_left and min_right arrays
    max_left = [0] * N
    min_right = [0] * N
    
    max_left[0] = A[0]
    for i in range(1, N):
        max_left[i] = max(max_left[i - 1], A[i])
    
    min_right[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], A[i])
    
    # Count the number of valid splits
    valid_splits = 0
    for i in range(N - 1):
        if max_left[i] < min_right[i + 1]:
            valid_splits += 1
    
    # If valid_splits is odd, Jeel wins (since Jeel plays first), else Ashish wins
    if valid_splits % 2 == 1:
        print("Jeel")
    else:
        print("Ashish")
