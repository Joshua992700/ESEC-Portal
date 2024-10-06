def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict:
            return [num_dict[num], i]
        else:
            num_dict[target - num] = i
    return []

nums = list(map(int, input().split()))
target = int(input())

result = twoSum(nums, target)

if result:
    print(f"Index1: {result[0]}")
    print(f"Index2: {result[1]}")
else:
    print("No two sum solution")

"""
Input 1
2 6 11 3
9

Result 1
Index1: 1
Index2: 3

Input 2
1 2 3 4 5
10

Result 2
No two sum solution
"""
