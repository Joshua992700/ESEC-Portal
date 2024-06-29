def print_pattern(n):
    current_num = 0

    # First part: increasing rows
    for i in range(n, 0, -1):
        for j in range(i):
            print(current_num, end=' ')
            current_num += 1
        print()
    
    # Second part: decreasing rows
    s = int(n*(n + 1)//2 - 1)
    for i in range(1,n+ 1):
        for j in range(i):
            print(s,end=" ")
            s -= 1
        print()

# Input handling
n = int(input())
print_pattern(n)

"""
Input
4

Output
0 1 2 3
4 5 6
7 8
9
9
8 7
6 5 4
3 2 1 0
"""
