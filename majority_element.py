def majorityElement(nums):
    # Step 1: Find a candidate for the majority element
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Step 2: Verify if the candidate is the majority element
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return 0

# Example usage
n = int(input())
nums = [int(input()) for i in range(n)]
print(majorityElement(nums)) 

"""
Input
9
1
2
3
4
4
4
4
3
4

Result
4
"""
