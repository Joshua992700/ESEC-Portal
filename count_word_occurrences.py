def count_word_occurrences(strings):
    words = strings.split()
    word_counts = {}
    for word in words:
        word = word.strip('.,!?;:')
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word} {count}")

# Test the function
strings = input()
count_word_occurrences(strings)

"""
Input
This There Next Where Why There Why

Result
This 1
There 2
Next 1
Where 1
Why 2
"""
