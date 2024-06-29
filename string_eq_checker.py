#Without In-Build Functions
def strings_are_equal_ignore_case(str1, str2):
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Convert both strings to lowercase manually and compare each character
    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]
        
        # Convert char1 to lowercase
        if 'A' <= char1 <= 'Z':
            char1 = chr(ord(char1) + 32)
        
        # Convert char2 to lowercase
        if 'A' <= char2 <= 'Z':
            char2 = chr(ord(char2) + 32)
        
        # Compare the characters
        if char1 != char2:
            return False
    
    return True

# Get user input for the two strings
string1 = input()
string2 = input()

# Check if the strings are equal, ignoring case
if strings_are_equal_ignore_case(string1, string2):
    print("Yes")
else:
    print("No")

#With In-Build Functions
"""
s1 = input().lower()
s2 = input().lower()

if s1 == s2:
  print("Yes")
else:
  print("No")

"""
