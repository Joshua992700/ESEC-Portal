n = int(input())
kids = [input().strip() for _ in range(n)]
gifts = int(input())
f = input().strip()
s = input().strip()

fi, si = kids.index(f), kids.index(s)
direction = "Clockwise" if (si - fi) % n == 2 else "Anti-clockwise"

count = {kid: 0 for kid in kids}
ci = fi
for _ in range(gifts):
    count[kids[ci]] += 1
    ci = (ci + 2) % n

max_kid = max(count, key=count.get)
print(direction)
print(max_kid)
