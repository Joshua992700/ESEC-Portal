def has_zero_sum_sub_array(arr):
    sum_set = set()
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in sum_set:
            return 'true'
        sum_set.add(current_sum)
    
    return 'false'

# Test the function
T = int(input())
for i in range(T):
     n = int(input())
     arr = list(map(int,input().split()))
     print(has_zero_sum_sub_array(arr))

"""
Input
1
6
1 2 3 -6 7 8

Result
true
"""
