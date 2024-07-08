def last_two_digits_of_fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # Initialize first two Fibonacci numbers
    fib_prev = 0
    fib_curr = 1
    
    # Compute Fibonacci numbers modulo 100 iteratively
    for _ in range(2, N + 1):
        fib_next = (fib_prev + fib_curr) % 100
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr

# Example usage:
N = int(input())
result = last_two_digits_of_fibonacci(N)
print(result)  # Output: 33
