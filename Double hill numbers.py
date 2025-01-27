n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=' ')

    for j in range(2 * (n - i - 1)):
        print(' ', end=' ')

    if i < n:
        for j in range(i + 1):
            print(i + 1, end=' ')

    print()

"""
Input	
4

Result
1             1
1 2         2 2
1 2 3     3 3 3
1 2 3 4 4 4 4 4
"""
