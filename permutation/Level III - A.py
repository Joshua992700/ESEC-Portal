from itertools import combinations

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    t = int(input())
    
    res = set()
    for i in range(1, n + 1):
        for r in combinations(arr, i):
            if sum(r) == t:
                res.add(tuple(sorted(r)))

    items = sorted(res)
    
    if not items:
        print("Empty")
    else:
        for item in items:
            print(f"({' '.join(map(str, item))})", end='')
        print()

"""
Input	
1
7
10 1 2 7 6 1 5
8

Result
(1 1 6)(1 2 5)(1 7)(2 6)
"""
