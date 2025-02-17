def add_binary_numbers(binary1, binary2):
    # Reverse the binary strings to start from the least significant digit
    binary1 = binary1[::-1]
    binary2 = binary2[::-1]
    
    # Initialize variables to store the result and carry
    result = []
    carry = 0
    
    # Iterate through the digits of the binary numbers
    for i in range(max(len(binary1), len(binary2))):
        # Get the current digits (or 0 if reached end of one binary number)
        digit1 = int(binary1[i]) if i < len(binary1) else 0
        digit2 = int(binary2[i]) if i < len(binary2) else 0
        
        # Add the digits along with the carry
        total = digit1 + digit2 + carry
        
        # Determine the result digit and carry for next iteration
        result.append(str(total % 2))
        carry = total // 2
    
    # If there is a carry after processing all digits, add it to the result
    if carry:
        result.append(str(carry))
    
    # Reverse the result to get the final binary number
    return ''.join(result[::-1])

# Input
binary1 = input() 
binary2 = input()

# Output
print(add_binary_numbers(binary1, binary2))
