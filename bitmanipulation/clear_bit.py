def clear_bit(n,k):
    return (n & (~(1 << (k-1))))

n = int(input())
k = int(input())

print(clear_bit(n,k))
