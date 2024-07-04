def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def least_significant_set_bit(n):
    i = 0
    while n:
        if n & 1:
            return i
        n >>= 1
        i += 1
    return -1

def most_significant_set_bit(n):
    i = 0
    while n:
        i += 1
        n >>= 1
    return i - 1 if i > 0 else -1

n = int(input())
a = count_set_bits(n)
b = least_significant_set_bit(n)
c = most_significant_set_bit(n)
print(f"{a}#{b}#{c}")
