def max_sum_subarray(arr, k):
    if k > len(arr):
        return "Invalid"
    max_sum = float('-inf')
    window_sum = sum(arr[:k])
    max_sum = max(max_sum, window_sum)
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

n = int(input())
a = list(map(int,input().split()))
k = int(input())
print(max_sum_subarray(a, k))
