s = input().split()

result = []
for i in s:
  if i.isnumeric():
    result.append(i)
  else:
    a = ''.join([c for c in i if c.isalpha()])[::-1]
    fw = []
    ai = 0
    
    for x in i:
      if x.isalpha():
        fw.append(a[ai])
        ai += 1 
      else:
        fw.append(x)
    result.append(''.join(fw).capitalize())

print(' '.join(result))
