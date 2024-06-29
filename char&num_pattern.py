def print_pattern(n):
    # Print letters and numbers in alternating rows, decrementing length each time
    for i in range(n, 0, -1):
        if i % 2 == 1:
            # Print letters from A onwards
            for j in range(i):
                print(chr(65 + j), end=" ")
        else:
            # Print numbers starting from 1
            for j in range(1, i + 1):
                print(j, end=" ")
        print()

# Input
n = int(input("Enter a number: "))

# Print the pattern
print_pattern(n)


"""
Sample Input
5

Sample Output
A B C D E
1 2 3 4
A B C
1 2
A
"""
