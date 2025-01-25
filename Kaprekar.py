n = int(input())

if n == 0:
    print("Not a Kaprekar Number")
else:
    sq = n * n
    s_sq = str(sq)
    d = len(str(n))
    l = s_sq[:-d] if s_sq[:-d] else '0'
    r = s_sq[-d:]


    if int(l) + int(r) == n:
        print("Kaprekar Number")
    else:
        print("Not a Kaprekar Number")

"""
Input 1
45
Result 1
Kaprekar Number
Input 2
13
Result 2
Not a Kaprekar Number
"""
