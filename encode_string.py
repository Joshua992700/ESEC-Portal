def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # Build the current number
        elif char == '[':
            # Push the current number and string onto the stack
            stack.append((current_str, current_num))
            current_str, current_num = "", 0  # Reset for the new segment
        elif char == ']':
            # Pop from the stack and construct the string
            last_str, num = stack.pop()
            current_str = last_str + current_str * num  # Repeat the current string
        else:
            current_str += char  # Build the current string

    return current_str

s = input()
x = decode_string(s)
print(x)

"""
Input
3[a]2[bc]

Result
aaabcbc
"""
