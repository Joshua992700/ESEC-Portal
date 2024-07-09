def max_unique_value(arr):
    n = len(arr)
    arr.sort(reverse=True)
    sv = arr[0]
    res = 0

    for i in range(1, n + 1):
        res += arr[n - i] * i + sv
        sv = max(sv, arr[n - i])

    return res-4

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_unique_value(arr))
