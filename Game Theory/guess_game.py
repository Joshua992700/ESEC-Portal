def getMoneyAmount(n):
    # dp[i][j] will store the minimum cost to guess between i and j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the DP table for ranges of length 2 to n
    for length in range(2, n + 1):  # length is the length of the range [start, end]
        for start in range(1, n - length + 2):  # start is the starting point of the range
            end = start + length - 1  # end is the end of the range
            
            # Initialize dp[start][end] with a large value
            dp[start][end] = float('inf')
            
            # Try each possible guess between start and end
            for guess in range(start, end):
                # The cost is the current guess + the worst case of the two subranges
                cost = guess + max(dp[start][guess - 1], dp[guess + 1][end])
                dp[start][end] = min(dp[start][end], cost)
    
    return dp[1][n]

# Test cases
n = int(input())
print(getMoneyAmount(n))
