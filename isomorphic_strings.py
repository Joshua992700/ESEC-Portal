def are_isomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# Test the function
a = input()
b = input()
print(str(are_isomorphic(a,b)).lower())

"""
Input	1
egg
add

Result 1
true

Input 2
foo
bar

Result 2
false

Input 3
tryit
abcda

Result 3
true
"""
