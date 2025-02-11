a = list(map(str, input().split(";")))[:-1]
i_lst, c_lst = [], []

for s in a:
    if s.startswith("int"):
        lst = i_lst
        s = s[4:]
    else:
        lst = c_lst
        s = s[5:]

    for x in s.split(','):
        lst.append(x if '=' in x else f"{x}=junk")

print("Integers")
print("\n".join(i_lst))
print("Characters")
print("\n".join(c_lst))

"""
(or)
# Read input and split by semicolon, removing the last empty entry
data = list(map(str, input().split(";")))[:-1]
int_list, char_list = [], []

# Process each entry in the input data
for entry in data:
    if entry.startswith("int"):
        current_list = int_list
        entry = entry[4:]  # Remove "int "
    else:
        current_list = char_list
        entry = entry[5:]  # Remove "char "

    # Split the entry by commas and process each variable
    for var in entry.split(','):
        # Append the variable to the current list, adding "=junk" if not initialized
        current_list.append(var if '=' in var else f"{var}=junk")

# Print the results for integers
print("Integers")
print("\n".join(int_list))

# Print the results for characters
print("Characters")
print("\n".join(char_list))
"""
