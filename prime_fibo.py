def prime_fibo(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    fibs = []
    if n >= 1:
        fibs.append(0)
    if n >= 2:
        fibs.append(1)
    for i in range(2, n):
        next_fib = fibs[i - 1] + fibs[i - 2]
        fibs.append(next_fib)

    for i in range(n):
        print(primes[i], fibs[i], end=" ")
    print()

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input())
prime_fibo(n)


"""
Sample Input 0

7
Sample Output 0

2 0 3 1 5 1 7 2 11 3 13 5 17 8
Explanation 0

2, 3, 5, 7, 11, 13, 17 are the first 7 prime numbers 0,1,1,2,3,5,8 are the first Fibonacci numbers The output is alternatively being printed as follows: 2 0 3 1 5 1 7 2 11 3 13 5 17 8
"""
