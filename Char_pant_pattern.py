def print_pattern(N):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(N):
        # First part: increasing alphabet from A
        first_part = alphabet[:N-i]
        
        # Middle part: spaces
        spaces = ' ' * (2 * i)
        
        # Second part: decreasing alphabet from G, F, E, ..., A
        second_part = alphabet[N-i-1::-1]
        
        # Combine and print the parts
        print(first_part + spaces + second_part)

# Input
N = int(input())

# Output
print_pattern(N)

"""
Input
7

Output
ABCDEFGGFEDCBA
ABCDEF  FEDCBA
ABCDE    EDCBA
ABCD      DCBA
ABC        CBA
AB          BA
A            A
"""
