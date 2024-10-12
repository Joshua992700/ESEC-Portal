def calculate_sum(s, m):
    total_sum = 0
    for string in s:
        value = 1
        for char in string:
            value *= (ord(char) ** m)
        total_sum += value
    return total_sum

def is_even(n):
    return n % 2 == 0

x = input()
s = eval(x)
m = int(input())
total_sum = calculate_sum(s, m)
if is_even(total_sum):
   print("EVEN")
else:
   print("ODD")

"""
Input
['ace','oqs','oqs']
5

Output
ODD
"""
