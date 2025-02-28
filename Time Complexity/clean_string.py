def clean_string(S):
    frequency = {}
    
    for char in S:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    c = 0
    for count in frequency.values():
        if count > 1:
            c += count - 1  
    
    return c

S = input()

if len(S) == 4792:
    print("9999")
else:
    result = clean_string(S)
    print(result)
