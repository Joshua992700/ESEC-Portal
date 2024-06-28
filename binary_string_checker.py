def is_binary_string(s):
    for char in s:
        if char not in ['0', '1']:
            return False
    return True

s = input()
if len(s) > 1 and len(s) < 100:
    print(is_binary_string(s))
else:
    print("Invalid input string length")
