def rotate_left(s, k):
    return s[k:] + s[:k]

def rotate_right(s, k):
    return s[-k:] + s[:-k]

n = int(input())

results = []
for i in range(n):
    s = input().strip()
    k = int(input().strip())

    if i % 2 == 0:
        results.append(rotate_left(s, k))
    else:
        results.append(rotate_right(s, k))

for res in results:
    print(res)


"""
Sample input:
5
Hello
1
Hello
1
ITVAC
2
ITVAC
2
Mercel
0

Sample Output:
elloH
oHell
VACIT
ACITV
Mercel

"""
