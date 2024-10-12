def print_pascal_triangle(n):
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    for row in triangle:
        print(' ' * (n - len(row)), end='')
        print(' '.join(str(num) for num in row))

n = int(input())
print("** Printing the pattern... **")
print_pascal_triangle(n)

"""
Input 
4

Result
** Printing the pattern... **
   1
  1 1
 1 2 1
1 3 3 1
"""
