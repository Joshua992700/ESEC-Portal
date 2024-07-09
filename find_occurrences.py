def find_occurrences(text, first, second):
    words = text.split()
    result = []
    
    for i in range(len(words) - 2):
        if words[i] == first and words[i+1] == second:
            result.append(words[i+2])
    
    return result

# Example usage
text1 = input()
first1 = input()
second1 = input()
x = find_occurrences(text1, first1, second1)
for i in x:
    print(i)
