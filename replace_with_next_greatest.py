def replace_with_next_greatest(arr):
    n = len(arr)
    for i in range(n - 1):
        max_val = max(arr[i + 1:])
        arr[i] = max_val
    arr[n - 1] = -1
    return arr

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
print("The modified array:")
print(' '.join(map(str, replace_with_next_greatest(arr))))
