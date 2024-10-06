def intersection(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

n1 = int(input())
n2 = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*intersection(arr1, arr2))

"""
Input
5
4
1 4 5 6 7
2 4 6 6

Result
4 6
"""
