a = input()
b = input().split()

def license(c, d):
    e = {}
    for i in c.lower():
        if i.isalpha():
            e[i] = e.get(i, 0) + 1
    g = None
    for h in d:
        i = {}
        for j in h:
            i[j] = i.get(j, 0) + 1
        if all(i.get(k, 0) >= e[k] for k in e):
            if g is None or len(h) < len(g):
                g = h
    return g

print(license(a, b))

"""
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]

Output: "steps"

Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.

"step" contains 't' and 'p', but only contains 1 's'.

"steps" contains 't', 'p', and both 's' characters.

"stripe" is missing an 's'.

"stepple" is missing an 's'.

Since "steps" is the only word containing all the letters, that is the answer.
"""
