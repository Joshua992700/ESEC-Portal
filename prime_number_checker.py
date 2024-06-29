def check_prime(n):
    if n <= 1:
        return "Not a Prime Number"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not a Prime Number"
    return "Prime Number"

n = int(input())
print(check_prime(n))
