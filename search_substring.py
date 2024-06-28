def find_substring(main_string, substring):
    # Find the position of the substring
    position = main_string.find(substring)
    
    # Check if the substring is found
    if position != -1:
        print(f"Starts at position {position+1}")
    else:
        print("Substring not found")

# Example usage
input_string1 = input()
substring1 = input()
find_substring(input_string1, substring1) 


"""
Input
HelloWorld
World

Result
Starts at position 6
"""
