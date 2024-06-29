n = int(input())
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print(j, end=' ')
  print()

for i in range(i+1):
  for j in range(n-i):
    print(j+1,end=' ')
  print()


"""
Input
3

Result
1 
1 2 
1 2 3 
1 2 3 
1 2 
1 
"""
