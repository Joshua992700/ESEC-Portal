def to_goat_latin(sentence):
    vowels = set('aeiouAEIOU')
    words = sentence.split()
    result = []
    for i, word in enumerate(words):
        if word[0] in vowels:
            result.append(word + 'ma' + 'a' * (i + 1))
        else:
            result.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
    return ' '.join(result)

n = input()
print(to_goat_latin(n))
