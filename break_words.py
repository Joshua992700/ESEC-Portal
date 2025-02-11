def words(s, d):
    def bt(start, p):
        if start == len(s):
            r.append(' '.join(p))
            return
        for end in range(start + 1, len(s) + 1):
            w = s[start:end]
            if w in d:
                bt(end, p + [w])

    r = []
    bt(0, [])
    return r

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    d = set(input().strip().split())
    s = input().strip()
    
    res = words(s, d)
    
    for sentence in res:
        print(sentence)
