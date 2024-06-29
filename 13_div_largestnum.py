n = int(input())

a = []
for i in range(n):
  if i % 13 == 0:
    a.append(int(i))

print(a[-1])

"""
Input
1000

Output
988
"""
