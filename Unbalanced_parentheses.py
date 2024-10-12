def remove_unbalanced_parentheses(s):
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(char)
            result.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                result.append(char)
            else:
                continue
        else:
            result.append(char)
    while stack:
        result.pop(result.index('('))
        stack.pop()
    return ''.join(result)

s = input()
print(remove_unbalanced_parentheses(s))

"""
Input
(((ab)

Result
(ab)
"""
