def total_good_flavours(n, k):
    total = 0
    for i in range(1, k + 1):
        total += comb(n, i)
    return total % 10000

from math import comb

n = int(input())
k = int(input())
print(total_good_flavours(n, k))
