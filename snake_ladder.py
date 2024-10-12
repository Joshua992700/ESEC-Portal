def word_break(s, word_dict):
    def backtrack(start, path):
        if start == len(s):
            result.append(' '.join(path))
            return
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict:
                backtrack(end, path + [word])

    result = []
    backtrack(0, [])
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    word_dict = set(input().split())
    s = input()
    sentences = word_break(s, word_dict)
    for sentence in sentences:
        print(sentence)

"""
Input
1
5
snake snakes and sand ladder
snakesandladder

Result
snake sand ladder
snakes and ladder
"""
