def is_valid(s):
    stack = []
    mapping = {']': '[', '}': '{', ')': '('}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

T = int(input())
for i in range(T):
    s = input()
    print(is_valid(s))

"""
Input1
1
({[]})

Result1
True

Input2
1
)))(((

Result2
False

Input3
2
()[]}{
[(){}]

Result3
False
True
"""
