def count_ascending_triples(arr):
    count = 0
    arr.sort()
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] < arr[j] < arr[k]:
                    count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
print(count_ascending_triples(arr))
