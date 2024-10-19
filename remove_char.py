def remove_chars(s1, s2):
    # Create a set of characters from s2 for faster lookup
    chars_to_remove = set(s2)
    # Build a new string with characters from s1 that are not in s2
    result = ''.join([char for char in s1 if char not in chars_to_remove])
    return result

# Input number of test cases
T = int(input())

# Loop through all test cases
for _ in range(T):
    s1 = input().strip()
    s2 = input().strip()
    # Print the result for each test case
    print(remove_chars(s1, s2))

"""
Input
1
itvaccodingteam
caw

Output
itvodingtem
"""
