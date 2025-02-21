t = int(input())
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

s = 0
c = 0

if t <= 0:
  print(c)
else:
  for j in range(n):
    s += arr[j]
    if s > t:
      break
    else:
      c += 1 
print(c)

"""
Input
8
5
1
2
3
4
5

Output
3
"""
