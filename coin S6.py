def optimal_strategy(arr, n):
    dp = [[0] * n for _ in range(n)]

    # Fill the table
    for i in range(n):  # 'i' is the new 'gap'
        for j in range(n - i):  # 'j' is the new 'i'
            k = j + i            # 'k' is the new 'j'

            # Base cases
            x = dp[j + 2][k] if (j + 2) <= k else 0
            y = dp[j + 1][k - 1] if (j + 1) <= (k - 1) else 0
            z = dp[j][k - 2] if j <= (k - 2) else 0

            dp[j][k] = max(arr[j] + min(x, y), arr[k] + min(y, z))

    return dp[0][n - 1]

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(optimal_strategy(A, N))
