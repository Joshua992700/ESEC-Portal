def main():
    n = int(input())

    # Printing the first part of the pattern
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1, 0, -1):
            print(" ", end="")

        # Print stars
        for j in range(i + 1):
            print("*", end="")
        print(" ", end="")

        # Print characters
        ch = chr(ord('A') + i)
        for j in range(i + 1):
            print(ch, end="")
            ch = chr(ord(ch) + 1)

        print()

    # Printing the second part of the pattern
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")

        # Print descending numbers
        for j in range(n, i, -1):
            print(j, end="")

        print(" ", end="")

        # Print odd numbers
        odd = 1 + 2 * i
        for j in range(i, n):
            print(odd, end="")
            odd += 2

        print()

if __name__ == "__main__":
    main()

"""
Output

    * A
   ** BC
  *** CDE
 **** DEFG
***** EFGHI
54321 13579
 5432 3579
  543 579
   54 79
    5 9

"""

