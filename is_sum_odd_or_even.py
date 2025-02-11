def is_sum_odd_or_even(strings, m):
    total_sum = 0

    for s in strings:
        value = 1
        for char in s:
            ord_value = ord(char)
            value *= ord_value ** m
        total_sum += value

    return "ODD" if total_sum % 2 != 0 else "EVEN"


l = eval(input())
k = int(input())
print(is_sum_odd_or_even(l,k))

"""
INPUT
['ace','oqs','oqs']
5

OUTPUT
ODD
"""
