def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

T = int(input())
for i in range(T):
    n = int(input())
    print("YES" if is_perfect(n) else "NO")


'''
Sample Input
3
6
5
28

Sample output:
YES
NO
YES

Explanation:
6=1+2+3,so it is perfect
5=1,so it is not perfect
28=1+2+4+7+14,so it is perfect

'''
