def print_pattern(n):
    # First part: increasing number of symbols
    for i in range(1, n + 1):
        if i % 2 == 1:
            # Print '*' pattern for odd rows
            print('* ' * i)
        else:
            # Print '#' pattern for even rows
            print('# ' * i)
    
    # Second part: decreasing number of symbols
    for i in range(n - 1, -1,-1):
        if i % 2 == 1:
            # Print '*' pattern for odd rows
            print('* ' * int(i+1))
        else:
            # Print '#' pattern for even rows
            print('# ' * int(i+1))

if __name__ == "__main__":
    n = int(input())
    print_pattern(n)

"""
Input
4

Output
*
# #
* * *
# # # #
* * * *
# # #
* *
#
"""
