def swap_consecutive_pairs(n):
    n = str(n)
    result = ''
    for i in range(0, len(n) - 1, 2):
        result += n[i+1] + n[i]
    if len(n) % 2!= 0:
        result += n[-1]
    return result

n = int(input())
print(swap_consecutive_pairs(n))
