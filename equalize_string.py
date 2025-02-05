def min_steps_to_make_equal(s1, s2):
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
        
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
        
    deletions = 0
    
    for char in freq1:
        if char in freq2:
            deletions += abs(freq1[char] - freq2[char])
        else:
            deletions += freq1[char]
    
    for char in freq2:
        if char not in freq1:
            deletions += freq2[char]
    
    return deletions

s1 = input()
s2 = input()
result = min_steps_to_make_equal(s1, s2)
print(result)
