n = int(input())
a = list(map(int,input().split()))

x = []
for i in range(0,int(n/2)):
    x.append(a[i])
    x.append(a[-i-1])
    
print(*x)
