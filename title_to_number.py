def title_to_number(columnTitle):
    result = 0
    for i, char in enumerate(columnTitle[::-1]):
        result += (ord(char) - 64) * (26 ** i)
    return result

columnTitle = input()
print(title_to_number(columnTitle))
