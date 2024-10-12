import math

def find_strong_numbers(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    strong_numbers = []
    for i in range(1, n + 1):
        sum_factorials = sum(factorial(int(digit)) for digit in str(i))
        if sum_factorials == i:
            strong_numbers.append(i)

    return strong_numbers

n = int(input())
print(*find_strong_numbers(n))

"""
Input
100

Result
1 2
"""
