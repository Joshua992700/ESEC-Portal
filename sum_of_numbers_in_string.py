s = input()

t = 0
c = ""

for i in s:
    if i.isdigit():
        c += i
    else:
        if c:
            t += int(c)
            c = ""

if c:
    t += int(c)

print(t)

"""
Input
343SATH98TRY4234HIS4

Result
4679
"""
