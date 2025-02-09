def unbalanced(s):
    st = []
    rm = set()

    for i, c in enumerate(s):
        if c == '(':
            st.append(i)
        elif c == ')':
            if st:
                st.pop()
            else:
                rm.add(i)

    rm.update(st)

    return ''.join(c for i, c in enumerate(s) if i not in rm)

s = input()
print(unbalanced(s))

"""
Input
(((ab)

Result
(ab)
"""
