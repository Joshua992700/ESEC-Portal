def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

n = int(input())
for _ in range(n):
    str1, str2 = input().split()
    print(are_anagrams(str1, str2))

"""
Input	
3
Hello hello
hello hello
HELLO hello

Result
False
True
False
"""
