def toggle_bit(n, k):
    mask = 1 << k
    result = n ^ mask
    
    return result

n = int(input())
k = int(input())
result = toggle_bit(number, n)
print(result)
