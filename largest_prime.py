def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def largest_prime_less_than_n(n):
    for i in range(n-1, 0, -1):
        if is_prime(i):
            return i

n = int(input())
print(largest_prime_less_than_n(n))

"""
Input
15

Output
13
"""
