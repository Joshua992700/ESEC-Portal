def print_diamond_pattern(rows, ch):
    spaces = rows - 1
    stars = 1

    for i in range(1, rows + 1):
        print(" " * spaces, end="")
        print(ch * stars)
        spaces -= 1
        stars += 2

    spaces = 1
    stars = rows * 2 - 3

    for i in range(1, rows):
        print(" " * spaces, end="")
        print(ch * stars)
        spaces += 1
        stars -= 2

rows = int(input())
ch = input()

print_diamond_pattern(rows, ch)


"""
Input
6
X

Output

     X
    XXX
   XXXXX
  XXXXXXX
 XXXXXXXXX
XXXXXXXXXXX
 XXXXXXXXX
  XXXXXXX
   XXXXX
    XXX
     X
"""
