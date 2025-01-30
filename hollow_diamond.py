n = int(input())

# Upper half of the diamond
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")

# Lower half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")
