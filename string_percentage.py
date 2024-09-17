def calculate_percentages(s, decimal_places):
    total_chars = len(s)
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = sum(1 for c in s if c.islower())
    digit_count = sum(1 for c in s if c.isdigit())
    other_count = total_chars - uppercase_count - lowercase_count - digit_count

    uppercase_percentage = (uppercase_count / total_chars) * 100
    lowercase_percentage = (lowercase_count / total_chars) * 100
    digit_percentage = (digit_count / total_chars) * 100
    other_percentage = (other_count / total_chars) * 100

    def format_percentage(p):
        decimal_part = p - int(p)
        if decimal_part == 0:
            return f"{int(p)}%"
        elif len(str(decimal_part).split('.')[1]) == 1:
            return f"{p:.1f}%"
        else:
            return f"{p:.2f}%"

    print(f"Uppercase letters are {format_percentage(uppercase_percentage)}")
    print(f"Lowercase letters are {format_percentage(lowercase_percentage)}")
    print(f"Digits Are {format_percentage(digit_percentage)}")
    print(f"Other Characters Are {format_percentage(other_percentage)}")

# Test cases
s = input()
calculate_percentages(s, 2)
