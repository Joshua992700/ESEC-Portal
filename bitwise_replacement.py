def bitwise_xor_of_others(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num

    for i in range(len(arr)):
        arr[i] = xor_all ^ arr[i]

    return arr

# Test the function
arr = list(map(int, input().split()))
print(bitwise_xor_of_others(arr))

"""
Input
1 2 3

Result
1 2 3
"""
