def right_rotate(arr, n, k):
    k = k % n
    return arr[-k:] + arr[:-k]

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(*right_rotate(arr, n, k))

"""
Input
5
12 13 14 15 16
3

Result
14 15 16 12 13 
"""
