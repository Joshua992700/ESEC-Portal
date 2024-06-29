n = int(input())
for i in range(1, n + 1):
    print('  ' * (n - i), end='')
    print('* ' * i)


"""
Input
3

Output
    * 
  * * 
* * *
"""
