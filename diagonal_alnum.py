# Create the alphabet-to-number dictionary
alphabet_to_number = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}

n = int(input())  # Input size of matrix

ch = ord('a')  # Start from 'a'

for i in range(n):
    for j in range(n):
        current_char = chr(ch)
        if i == j:
            print(alphabet_to_number[current_char], end=' ')  # Diagonal: print number
        else:
            print(current_char, end=' ')  # Non-diagonal: print letter
        ch += 1
        if ch > ord('z'):
            ch = ord('a')  # Wrap around
    print()
