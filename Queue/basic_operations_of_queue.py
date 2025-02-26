q = []

while True:
  ch = int(input())

if ch == 1:
  t = int(input())
  q.append(t)
elif ch == 2:
  q.pop(0)
elif ch == 3:
  print(*q)
else:
  break
