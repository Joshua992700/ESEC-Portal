n = input()
if len(n) not in [2, 4]:
    print(-1)
else:
    result = ""
    for i in range(0, len(n), 2):
        result += n[i+1] + n[i]
    print(result)
