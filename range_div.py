a = int(input())
b = int(input())
k = int(input())

c = []
for i in range(a,b+1):
    if i % k == 0:
        c.append(int(i))

print(len(c))
