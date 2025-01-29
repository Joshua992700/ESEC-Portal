def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_additive_prime(n):
    """Check if a number is an additive prime"""
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(n))
    # Check if the number and the sum of its digits are prime
    return is_prime(n) and is_prime(sum_of_digits)

def find_additive_primes(arr):
    """Find additive primes in an array"""
    additive_primes = [num for num in arr if is_additive_prime(num)]
    return additive_primes

n = int(input())
arr = list(map(int, input().split()))
print(*find_additive_primes(arr))

"""
Input
7
2 4 6 11 12 18 7

Result
2 11 7

(OR)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_additive_primes(arr):
    additive_primes = []
    for num in arr:
        if is_prime(num) or (not is_prime(num) and is_prime(sum_of_digits(num))):
            additive_primes.append(num)
    return additive_primes

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_additive_primes(arr)
    print(*result) 
"""
