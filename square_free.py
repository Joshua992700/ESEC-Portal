def is_square_free(num):
    # Check divisibility by perfect squares greater than 1
    for i in range(2, int(num**0.5) + 1):
        if num % (i * i) == 0:
            return False
    return True

def count_square_free_divisors(n):
    square_free_count = 0
    # Find all divisors of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i is a divisor
            if i > 1 and is_square_free(i):
                square_free_count += 1
            # n // i is also a divisor
            if i != n // i:  # Avoid counting the square root twice
                if (n // i) > 1 and is_square_free(n // i):
                    square_free_count += 1
    return square_free_count

# Input
N = int(input())
result = count_square_free_divisors(N)
print(result)
