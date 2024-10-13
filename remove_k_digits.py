def removeKdigits(num, k):
    stack = []
    for n in num:
        while k and stack and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k:
        stack = stack[:-k]
    return ''.join(stack).lstrip('0') or '0'

num = input()
k = int(input())

print(removeKdigits(num, k))

"""
Input
10200
1

Result
200
"""
