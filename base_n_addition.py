def base_n_to_decimal(number_str, base):
    return int(number_str, base)

def decimal_to_base_n(number, base):
    if number == 0:
        return "0"
    digits = []
    while number > 0:
        digits.append(str(number % base))
        number //= base
    return ''.join(reversed(digits))

# Input
a = input().strip()
b = input().strip()
base = int(input().strip())

num1 = base_n_to_decimal(a, base)
num2 = base_n_to_decimal(b, base)
total = num1 + num2

if total < 0:
    print("Invalid Input")
else:
    print(decimal_to_base_n(total, base))
