def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

n = int(input())
print_fibonacci(n)


"""
Sample Input1: 
5

Sample Output1:  
0 1 1 2 3 
"""
