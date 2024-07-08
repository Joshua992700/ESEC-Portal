def trap_water(arr):
    n = len(arr)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = arr[0]
    right_max[n-1] = arr[n-1]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]
    return water

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(trap_water(arr))
