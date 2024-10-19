def max_money(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses[0], houses[1])

    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return dp[-1]

# Example usage
t = int(input())

for _ in range(t):
    n, money = map(int, input().split())
    houses = [money] * n
    result = max_money(houses)
    print(result)

"""
Input
1
5 10

Output
30
"""
