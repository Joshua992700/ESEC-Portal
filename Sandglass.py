n = int(input())

# Print the upper half of the pattern
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)

# Print the lower half of the pattern
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
