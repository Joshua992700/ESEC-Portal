def print_pattern(n):
    # Function to print each line of the pattern
    def print_line(start, count):
        numbers = [str(start + i) for i in range(count)]
        print('*'.join(numbers))

    current_num = 1
    # Print the top part of the pattern
    for i in range(1, n + 1):
        print_line(current_num, i)
        current_num += i

    # Print the bottom part of the pattern
    for i in range(n, 0, -1):
        current_num -= i
        print_line(current_num, i)

# Read input
n = int(input())

# Print the pattern
print_pattern(n)


"""
INPUT
5

OUTPUT
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
"""
