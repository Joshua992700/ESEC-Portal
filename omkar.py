for _ in range(int(input()):
    n = int(input())
    a = list(map(int, input().split()))
    if all(x == a[0] for x in a):
        print(n)
    else:
        print(1)
