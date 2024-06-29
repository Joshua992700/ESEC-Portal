# Get user input for hours, minutes, and seconds
time_input = input()

# Split the input string into hours, minutes, and seconds
hours, minutes, seconds = map(int, time_input.split(':'))

# Convert hours, minutes, and seconds to total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)
