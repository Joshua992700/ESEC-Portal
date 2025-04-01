def rob_linear(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[-1]

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    case1 = rob_linear(nums[1:])
    case2 = rob_linear(nums[:-1])
    
    return max(case1, case2)

nums = list(map(int, input().split(',')))
print(rob(nums))
