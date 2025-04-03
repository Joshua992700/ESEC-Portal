def traverse(ind, w):
    if ind == 0:
        if w >= wt[0]:
            return val[0]
        return 0

    if dp[ind][w] != -1:
        return dp[ind][w]

    not_take = traverse(ind - 1, w)

    take = float('-inf')
    if wt[ind] <= w:
        take = val[ind] + traverse(ind - 1, w - wt[ind])

    dp[ind][w] = max(take, not_take)
    return dp[ind][w]

val = list(eval(input()))
wt = list(map(int, input()[1:-1].split(",")))
cap = int(input())

dp = [[-1 for _ in range(cap + 1)] for _ in range(len(val))]

result = traverse(len(val) - 1, cap)
print(result)
