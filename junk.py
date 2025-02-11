a = list(map(str, input().split(";")))[:-1]
i_lst, c_lst = [], []

for s in a:
    if s.startswith("int"):
        lst = i_lst
        s = s[4:]
    else:
        lst = c_lst
        s = s[5:]

    for x in s.split(','):
        lst.append(x if '=' in x else f"{x}=junk")

print("Integers")
print("\n".join(i_lst))
print("Characters")
print("\n".join(c_lst))
