def three_sum_closest(arr, target):
    arr.sort()
    max_sum = float('-inf')
    for i in range(len(arr) - 2):
        l, r = i + 1, len(arr) - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == target:
                return s
            if abs(s - target) < abs(max_sum - target):
                max_sum = s
            if s < target:
                l += 1
            else:
                r -= 1
    return max_sum

t, target = map(int, input().split())
arr = list(map(int, input().split()))
print(three_sum_closest(arr, target))


"""
Sample input:

6 2
-7 9 8 3 1 1
Output:
2

Explanation
-7+8+1= 2 
which is the closest to the expected input. So this is the output

"""
