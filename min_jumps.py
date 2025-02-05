def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:
                return jumps
            
        if current_end <= i and arr[i] == 0:
            return -1

    return -1 if current_end < n - 1 else jumps

# Read input
T = int(input())
results = []
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_jumps(arr)
    results.append(result)

# Print results
for res in results:
    print(res)
