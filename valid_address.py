import re

def is_valid_address(address):
    pattern = r'^\d+[a-zA-Z] Sector [a-zA-Z]$'
    return bool(re.match(pattern, address))

address = input()
print(is_valid_address(address))

"""
Input
45 Sector X

Output
True
"""
