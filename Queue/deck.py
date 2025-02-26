n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

res = []
for i in reversed(arr):
    if res:
        res.append(res.pop(0))
    res.append(i)

print(*res[::-1])
