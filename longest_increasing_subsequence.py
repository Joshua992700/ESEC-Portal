def longest_increasing_subsequence(arr):
    N = len(arr)
    if N == 0:
        return 0
    
    # DP array initialized to 1 (each element is a subsequence of length 1)
    dp = [1] * N
    
    # Loop through all elements to build the dp array
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The length of the longest increasing subsequence is the max value in dp array
    return max(dp)

n = int(input())
arr = [int(input()) for _ in range(n)]
print(longest_increasing_subsequence(arr)) 
