def sort_words_caps(sentence):
    words = sentence.split()
    words.sort(key=lambda x: (x.lower(), x))
    return ' '.join(words)

# Test the function
sentence = input()
print(sort_words_caps(sentence))

"""
Input
Cleanliness is next to Godliness

Result
Cleanliness Godliness is next to
"""
