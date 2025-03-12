def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

n = int(input())
dp = [0] * n

for i in range(n):
    dp[i] = fact(int(input()))

for i in dp:
    print(i)
