T = int(input())

for _ in range(T):
    s = input()
    m = {')': '(', '}': '{', ']': '['}
    
    c = True
    st = []
    for i in s:
        if i in m.values():
            st.append(i)
        elif i in m.keys():
            if not st or st.pop() != m[i]:
                c = False
                break
    
    print(c and not st)
