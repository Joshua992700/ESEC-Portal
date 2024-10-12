n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort(reverse=True)
if len(arr) < 2:
    print(-1)
else:
    print(arr[1])  # Print the second largest number

"""
Input
7
1 2 3 4 4 2 3

Result
3
"""
