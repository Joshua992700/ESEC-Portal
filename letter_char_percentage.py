s = input()

u = 0
l = 0
d = 0
c = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    elif i.isdigit():
        d += 1
    else:
        c += 1

u = (u/len(s))*100
l = (l/len(s))*100
d = (d/len(s))*100
c = (c/len(s))*100

print(f"Uppercase letters are {format(u, '.2f').rstrip('0').rstrip('.') if u % 1 != 0 else int(u)}%")
print(f"Lowercase letters are {format(l, '.2f').rstrip('0').rstrip('.') if l % 1 != 0 else int(l)}%")
print(f"Digits Are {format(d, '.2f').rstrip('0').rstrip('.') if d % 1 != 0 else int(d)}%")
print(f"Other Characters Are {format(c, '.2f').rstrip('0').rstrip('.') if c % 1 != 0 else int(c)}%")

"""
Input
My e-mail : eMail_Address321@anymail.com

Result
Uppercase letters are 7.5% 
Lowercase letters are 65%
Digits Are 7.5%
Other Characters Are 20%
"""
