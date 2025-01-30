arr = list(map(int,input().split()))

x = 0
for i in range(len(arr)):
    x ^= arr[i]
    
for i in range(len(arr)):
    arr[i] = x ^ arr[i]
    
print(*arr)
