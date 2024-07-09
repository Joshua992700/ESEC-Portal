def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    result_sum = 0

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                result_sum = current_sum
            elif abs(target - current_sum) == abs(target - closest_sum):
                result_sum = max(result_sum, current_sum)

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return result_sum

# Input
T, target = map(int, input().split())
nums = list(map(int, input().split()))

# Output
print(threeSumClosest(nums, target))
