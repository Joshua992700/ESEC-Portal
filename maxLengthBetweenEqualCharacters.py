def maxLengthBetweenEqualCharacters(s):
    max_length = -1
    char_index = {}
    
    for i, c in enumerate(s):
        if c in char_index:
            max_length = max(max_length, i - char_index[c] - 1)
        else:
            char_index[c] = i
    
    return max_length

# Test the function
s = input()
print(maxLengthBetweenEqualCharacters(s))
