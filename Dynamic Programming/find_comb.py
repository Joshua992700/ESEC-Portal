def find_comb(s, nums):
    dp = [None] * (s + 1)
    dp[0] = []

    for num in nums:
        for j in range(num, s + 1):
            if dp[j - num] is not None:
                new_comb = dp[j - num] + [num]
                if dp[j] is None or len(new_comb) < len(dp[j]):
                    dp[j] = new_comb

    return sorted(dp[s]) if dp[s] is not None else None

s = int(input())
nums = list(map(int,input().split(',')))

res = find_comb(s, nums)
if res is not None:
    print(f"{','.join(map(str, res))},")
else:
    print(f"{s}: No combination found,")
