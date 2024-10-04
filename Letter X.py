n = int(input())

# Calculate the height of the pattern
height = 2 * (n - 1) + 1

# Print the upper half including the middle row
for i in range(n):
    for j in range(height):
        if j == i or j == height - i - 1:
            print("* ", end="")
        else:
            print(" ", end="")
    print()

# Print the lower half excluding the middle row
for i in range(n - 2, -1, -1):
    for j in range(height):
        if j == i or j == height - i - 1:
            print("* ", end="")
        else:
            print(" ", end="")
    print()
