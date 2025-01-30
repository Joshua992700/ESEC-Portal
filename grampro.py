s = input()
mid = len(s) // 2

current_string = ''
for i in range(mid, len(s)):
    current_string += s[i]
    print(current_string)

for i in range(0, mid):
    current_string += s[i]
    print(current_string)
