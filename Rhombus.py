n = int(input())

for i in range(n):
  for j in range(n-i):
    print(" ",end=' ')
  
  start = 65
  for j in range(i+1):
    print(chr(start),end=' ')
    start += 1 
  s2 = 1
  for j in range(i+1):
    print(s2+j,end=' ')
  print()

num = 1
for i in range(n):
  for j in range(i+1):
    print(" ",end=' ')
  
  for j in range(n-i):
    print("*",end=' ')
  
  for j in range(n-i):
    print(num,end=' ')
    num += 1
  print()
