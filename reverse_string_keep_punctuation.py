def reverse_string_keep_punctuation(s):
    # Convert the string to a list of characters for easy manipulation
    s = list(s)
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move the left pointer until it points to an alphanumeric character
        if not s[left].isalnum():
            left += 1
            continue
        
        # Move the right pointer until it points to an alphanumeric character
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    # Convert the list back to a string
    return ''.join(s)

# Read input
input_string = input()

# Print the modified string
print(reverse_string_keep_punctuation(input_string))
