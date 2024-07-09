def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]  # Start with the first string as the initial prefix
    
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:  # Check if current prefix matches
            prefix = prefix[:-1]  # Reduce prefix length by one character
        
        if prefix == "":  # If at any point prefix becomes empty, no common prefix
            return ""
    
    return prefix

# Example usage:
strs1 = input().split()

print(longest_common_prefix(strs1))
