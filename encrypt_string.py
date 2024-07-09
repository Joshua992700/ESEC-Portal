def encrypt_string(s: str) -> str:
    encrypted = ''
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encrypted += s[i - 1] + hex(count)[2:].lower()
            count = 1

    encrypted += s[-1] + hex(count)[2:].lower()
    return encrypted[::-1]

# Test case
s = input()
print(encrypt_string(s))  # Output: ba
