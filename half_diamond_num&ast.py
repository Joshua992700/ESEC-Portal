def print_number_asterisk_pattern(n):
    current_number = 1
    for i in range(1, n + 1):
        # Print numbers for the current row
        for j in range(i):
            print(current_number, end=" ")
            current_number += 1
        
        # Print spaces to create the right alignment for asterisks
        spaces = (n - i) * 2  # Calculate the number of spaces
        print("  " * spaces, end="")

        # Print asterisks for the current row
        for j in range(i):
            print("*", end=" ")

        # Move to the next line after each row
        print()

n = int(input())
print_number_asterisk_pattern(n)

"""
Input
3

Output
1         * 
2 3     * * 
4 5 6 * * * 
"""
