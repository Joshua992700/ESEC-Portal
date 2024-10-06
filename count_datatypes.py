def count_data_types(input_string):
    # Split the input string into substrings
    substrings = input_string.split()

    # Initialize counters for each data type
    string_count = 0
    integer_count = 0
    double_count = 0

    # Iterate over the substrings and identify their data types
    for substring in substrings:
        try:
            # Try to convert the substring to an integer
            int(substring)
            integer_count += 1
        except ValueError:
            try:
                # Try to convert the substring to a float
                float(substring)
                double_count += 1
            except ValueError:
                # If the substring cannot be converted to a number, it's a string
                string_count += 1

    # Print the results
    print(f"string {string_count}")
    print(f"integer {integer_count}")
    print(f"double {double_count}")

# Test the function
s = input()
count_data_types(s)

"""
Input	
can you give me 10 bucks puff in 7.5 or 7

Result
string 8 
integer 2 
double 1
"""
