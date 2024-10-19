def has_consecutive_three_digits(num):
    # Convert the number to a string to iterate through digits
    num_str = str(num)

    for i in range(len(num_str) - 2):
        # Get three consecutive digits
        first = int(num_str[i])
        second = int(num_str[i + 1])
        third = int(num_str[i + 2])

        # Check for increasing order
        if first + 1 == second and second + 1 == third:
            return 'Yes'

        # Check for decreasing order
        if first - 1 == second and second - 1 == third:
            return 'Yes'

    return 'No'  # Return 'No' if no such sequence is found

# Example usage
input_number = input()
result = has_consecutive_three_digits(input_number)
print(result)

"""
Input
1230

Output
Yes
"""
