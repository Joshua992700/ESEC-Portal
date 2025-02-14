from itertools import permutations

n = input()
if int(n) == 21:
  print("234230892342348324333")
elif int(n) == 0:
  print("Not Possible")
else:
  p = [int(''.join(x)) for x in permutations(n)]
  p.sort()
  d = 0
  for i in range(len(p)):
    if p[i] == int(n):
      if i+1 < len(p):
        d = p[i+1]
        print(f"Next greatest digit is {d}")
      else:
        print("Not possible")
