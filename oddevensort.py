n = int(input())
a = [int(x) for x in input().split()]
for i in range(0, n, 2):
    for j in range(i + 2, n, 2):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

for i in range(1, n, 2):
    for j in range(i + 2, n, 2):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(' '.join(map(str, a)))


"""
Sample Input 1:
9
1 2 3 4 5 6 7 8 9

Sample Output 1:
9 2 7 4 5 6 3 8 1

"""
