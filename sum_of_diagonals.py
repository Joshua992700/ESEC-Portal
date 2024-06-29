n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

s = 0
for i in range(0,n):
    for j in range(0,n):
        if (i == j):
            s += a[i][j]

print("Addition of the right Diagonal elements is:",s)
