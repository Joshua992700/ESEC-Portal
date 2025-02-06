def longest_palindrome(s):
    char_counts = {}
    
    # Count character occurrences manually
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    length = 0
    odd_found = False

    for count in char_counts.values():
        if count % 2 == 0:
            length += count  # Use all even occurrences
        else:
            length += count - 1  # Use the largest even part
            odd_found = True  # Mark that we have an odd count

    return length + 1 if odd_found else length

# Example usage
s = input()
print(longest_palindrome(s))
