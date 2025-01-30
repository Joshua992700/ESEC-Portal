n = int(input())

for j in range(n):
    print(j + 1, end=' ')
print()

for i in range(1, n - 1):
    print('  ' * (n - 1 - i)+ str(n - i), end=' ')
    print()

for j in range(1,n+1):
    print(j, end=' ')
print()
