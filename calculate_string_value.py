def calculate_string_value(s, m):
    total = 1
    for char in s:
        total *= ord(char) ** m
    return total

def check_sum_parity(s, m):
    total_sum = 0
    for string in s:
        total_sum += calculate_string_value(string, m)
    
    if total_sum % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Input
s = ['ace', 'oqs', 'oqs']  # Example array of strings
m = 5  # Exponent

# Calculate result and print it
result = check_sum_parity(s, m)
print(result)
