def highest_frequency_word(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.lower()
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    max_freq = max(word_freq.values(), default=0)
    if max_freq == 1:
        return None
    else:
        return max(word_freq, key=word_freq.get)

text = input()
print(str(highest_frequency_word(text)).title())
