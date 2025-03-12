def can_construct(target, words):
    dp = [False] * (len(target) + 1)
    dp[0] = True

    for i in range(1, len(target) + 1):
        for word in words:
            if dp[i - len(word)] and target[i - len(word):i] == word:
                dp[i] = True
                break

    return "YES" if dp[len(target)] else "NO"


target = input()
words_input = input()
words = [word.strip() for word in words_input.split(',')]
    
result = can_construct(target, words)
print(result)
