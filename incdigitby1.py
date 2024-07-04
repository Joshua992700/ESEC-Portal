s = input()
result = ""
for c in s:
    if c == "9":
        result += c
    else:
        result += chr(ord(c) + 1)
print(result)
