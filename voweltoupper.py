T = int(input())

for _ in range(T):
    s = input()
    result = ""
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    print(result)
