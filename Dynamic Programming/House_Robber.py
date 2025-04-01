def rob_linear(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev1, prev2 = 0, 0
    
    for num in nums:
        temp = prev1
        prev1 = max(prev1, prev2 + num)  
        prev2 = temp
    
    return prev1

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    case1 = rob_linear(nums[1:])
    case2 = rob_linear(nums[:-1])
    
    return max(case1, case2)

nums = list(map(int, input().split(',')))
print(rob(nums))
