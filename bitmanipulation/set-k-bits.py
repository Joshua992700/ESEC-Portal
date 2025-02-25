def set_kth_bit(n, k):
    x = 2 ** (k - 1)
    if n & x:
        return n  
    else:
        return n + x 

n = int(input())
k = int(input())
print(set_kth_bit(n,k))
