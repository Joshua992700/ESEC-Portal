def min_sum_unique_elements(arr):
    arr.sort()
    res = []
    for num in arr:
        while num in res:
            num += 1
        res.append(num)
    return sum(res)

arr = list(map(int,input().split()))
print(min_sum_unique_elements(arr))
