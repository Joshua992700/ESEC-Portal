def can_construct(target, words):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # Base case: empty string can be formed

    for i in range(1, len(target) + 1):
        for word in words:
            if dp[i - len(word)] and target[i - len(word):i] == word:
                dp[i] = True
                break  # No need to check further if we found a match

    return "YES" if dp[len(target)] else "NO"


target = input()
words_input = input()
words = [word.strip() for word in words_input.split(',')]
    
result = can_construct(target, words)
print(result)
