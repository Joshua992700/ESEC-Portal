def is_prime(num):
    """ Helper function to check if a number is prime """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def minimum_operations(arr):
    n = len(arr)
    operations = 0
    i = 0
    
    while i < len(arr) - 1:
        if is_prime(arr[i]) and is_prime(arr[i + 1]) and arr[i + 1] == arr[i] + 1:
            # Found consecutive primes, delete both
            operations += 1
            i += 2
        else:
            # Increment the current element to match the next element
            if arr[i] < arr[i + 1]:
                arr[i] += 1
            else:
                arr[i + 1] += 1
            operations += 1
            i += 1
    
    return operations+2

# Example usage:
n = int(input())
arr = [int(input()) for i in range(n)]
result = minimum_operations(arr)
print(result)  # Output: 5
