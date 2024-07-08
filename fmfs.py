def rearrange_array(arr):
    arr.sort()
    result = []
    while arr:
        result.append(arr.pop())
        if arr:
            result.append(arr.pop(0))
    return result

N = int(input())
arr = list(map(int,input().split()))
result = rearrange_array(arr)
print(' '.join(map(str, result)))
