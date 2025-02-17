s = input().strip()

if len(s) < 10:
    print("Invalid")
else:
    seen = set()
    r = []
    seen_order = set()  # To maintain order of first occurrence

    for i in range(len(s) - 9):
        seq = s[i:i+10]
        if seq in seen and seq not in seen_order:
            r.append(seq)
            seen_order.add(seq)
        else:
            seen.add(seq)

    if r:
        for i in r:
            print(i)
    else:
        print("No repeated sequences")

"""
Input 1:
ACGAATTCCGACGAATTCCG

Output 1:
ACGAATTCCG

Input 2:
AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT

Output 2:
AAAAACCCCC
CCCCCAAAAA
"""
