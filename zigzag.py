def zig_zag_array(arr):
    for i in range(len(arr) - 1):
        if i % 2 == 0 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i % 2 != 0 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(zig_zag_array(arr))

"""
Input
5
31
32
33
34
35

Result	
[31, 33, 32, 35, 34]
"""
