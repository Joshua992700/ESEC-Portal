a = list(map(str, input().split(";")))[:-1]
i_lst, c_lst = [], []

for s in a:
    if s[:3] == "int":
        s = s[4:].split(',')
        for x in s:
            if '=' not in x:
                x += "=junk"
            i_lst.append(x)
    else:
        s = s[5:].split(',')
        for x in s:
            if '=' not in x:
                x += "=junk"
            c_lst.append(x)

print("Integers")
for x in i_lst:
    print(x)
print("Characters")
for x in c_lst:
    print(x)
