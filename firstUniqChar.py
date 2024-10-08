def firstUniqChar(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i+1
    return -1

s = input()
print(firstUniqChar(s))

"""
Input: s = "itvac"
Output: 1

Input: s = "lovecodinglife"
Output: 3

Input: s = "aabb"
Output: -1
"""
