import re

def extract_integers(s):
    integers = re.findall('\d+', s)
    return ' '.join(integers)

# Test cases
t = int(input())
for _ in range(t):
    s = input()
    print(extract_integers(s))
