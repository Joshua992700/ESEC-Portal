def maxLengthBetweenEqualCharacters(s: str) -> int:
    char_index = {}
    max_length = -1
    for i, char in enumerate(s):
        if char in char_index:
            max_length = max(max_length, i - char_index[char] - 1)
        else:
            char_index[char] = i
    return max_length

n = input()
print(maxLengthBetweenEqualCharacters(n))
