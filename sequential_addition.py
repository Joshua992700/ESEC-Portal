def find_c(x,t,s,p,r):
  if t == 0:
    r.append(p)
    return
  if t < 0:
    return
  
  for i in range(s,len(x)):
    find_c(x,t-x[i],i+1,p+[x[i]],r)
    
a = list(map(int,input().split()))
t = int(input())

ans = []
find_c(a,t,0,[],ans)

if ans:
  for i in ans:
    print(list(i))
else:
  print("-1")

"""
Input
1 2 3 4 5
9

Output
[1, 3, 5]
[2, 3, 4]
[4, 5]
"""
