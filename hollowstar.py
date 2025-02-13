N = int(input())

# Upper part of the pattern
for i in range(N):
    # Print left stars
    print("*" * (N - i), end=" ")
    # Print spaces in the middle
    print(" " * (2 * i), end="")
    # Print right stars
    print("*" * (N - i))

# Lower part of the pattern
for i in range(N):
    # Print left stars
    print("*" * (i + 1), end=" ")
    # Print spaces in the middle
    print(" " * (2 * (N - i - 1)), end="")
    # Print right stars
    print("*" * (i + 1))


#OUTPUT
"""
Input: 
5
Output:
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
"""
