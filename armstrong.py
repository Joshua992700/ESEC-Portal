def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == number

def print_armstrong_numbers(start, end):
    print(f"Armstrong number between {start} to {end} are:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number,end=" ")

# Test the function with a specific range
start_range = int(input())
end_range = int(input())
print_armstrong_numbers(start_range, end_range)

"""
Input
200
500

Output
Armstrong number between 200 to 500 are:
370 371 407
"""
