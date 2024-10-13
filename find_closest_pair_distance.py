def find_closest_pair_distance(arr):
    arr.sort()
    min_distance = float('inf')
    for i in range(len(arr) - 1):
        distance = abs(arr[i] - arr[i + 1])
        if distance < min_distance:
            min_distance = distance
    return min_distance

n = int(input())
a = list(map(int,input().split()))
print(find_closest_pair_distance(a))

"""
Input
3
-10 0 11

Output
10
"""
