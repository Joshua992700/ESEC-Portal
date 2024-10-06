def min_difference_pair(arr):
    if len(set(arr)) != len(arr):
        return "Invalid value in array!!!"
    arr.sort()
    return min(arr[i+1] - arr[i] for i in range(len(arr) - 1))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_difference_pair(arr))

"""
Input
1
6
100 301 501 709 7878 2343

Result
200
"""
