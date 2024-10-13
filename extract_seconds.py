def extract_seconds(sentence):
    words = sentence.split()
    for word in words:
        if ':' in word:
            time_parts = word.split(':')
            if len(time_parts) == 3 or len(time_parts) == 4:
                if len(time_parts) == 3:
                    hours, minutes, seconds = time_parts
                else:
                    hours, minutes, seconds, _ = time_parts
                if seconds.isdigit():
                    return int(seconds)
    return None

# Input
sentence = input().strip()

# Output
result = extract_seconds(sentence)
if result is not None:
    print(result)
else:
    print("No seconds found in the sentence.")

"""
Input
Today the time is 09:11:33: Check it out

Output
33
"""
