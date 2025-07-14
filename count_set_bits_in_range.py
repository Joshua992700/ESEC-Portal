def count_set_bits_in_range(n, l, r):
    mask_r = (1 << r) - 1
    mask_l = (1 << (l - 1)) - 1
    mask = mask_r & (~mask_l)
    masked_bits = n & mask
    
    shifted_bits = masked_bits >> (l - 1)
    
    return bin(shifted_bits).count('1')

n = int(input())
l, r = map(int,input().split())
print(count_set_bits_in_range(n, l, r))
