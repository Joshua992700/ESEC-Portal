def vowelStrings(words, queries):
    vowels = set('aeiou')
    count = [0] * len(words)
    for i, word in enumerate(words):
        if word[0] in vowels and word[-1] in vowels:
            count[i] = 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    ans = []
    for li, ri in queries:
        if li == 0:
            ans.append(count[ri])
        else:
            ans.append(count[ri] - count[li - 1])
    return ans

# Test the function
a = input()
b = input()
words = eval(a)
queries = eval(b)
print(vowelStrings(words, queries))

"""
Input
["aba","bcb","ece","aa","e"]
[[0,2],[1,4],[1,1]]

Result
[2, 3, 0]
"""
