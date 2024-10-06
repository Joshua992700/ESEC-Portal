import re

def extract_numbers(s):
    numbers = re.findall(r'\d+', s)
    numbers_without_9 = [num for num in numbers if '9' not in num]
    if numbers_without_9:
        return numbers_without_9
    else:
        return [-1]

# Test the function
T = int(input())
for _ in range(T):
    s = input()
    result = extract_numbers(s)
    print(*result)

"""
Input
2
This is alpha 5057 and 97
GSLV is a satellite

Result
5057
-1
"""
