def print_repeated_letters():
    string = input()
    char_count = {}
    repeated_letters = []

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            repeated_letters.append(char)

    if repeated_letters:
        print(''.join(repeated_letters))
    else:
        print("None")

print_repeated_letters()
