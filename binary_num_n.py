def print_binary_pattern(n):
    for i in range(n):
        for j in range(n):
            # Determine whether to print '1' or '0' based on the sum of the current row and column indices
            if (i + j) % 2 == 0:
                print('1', end='')
            else:
                print('0', end='')
        print()

# Input from the user
n = int(input())

print_binary_pattern(n)


"""
Input
5

Output
10101
01010
10101
01010
10101
"""
