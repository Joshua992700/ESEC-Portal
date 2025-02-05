s = eval(input())
k = int(input())

res = []
for i in range(len(s)-k+1):
    x = s[i:i + k]
    res.append(max(x))

print(','.join(map(str,res)))
