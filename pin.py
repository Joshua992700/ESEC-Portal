def cumulative_sum(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def replace_odd_with_alphabet(pin_list):
    alphabet_map = {1: 'a', 3: 'c', 5: 'e', 7: 'g', 9: 'i'}
    pin_str = ""
    for num in pin_list:
        pin_str += alphabet_map.get(num, str(num))
    return pin_str

# Input
n = int(input())  # Number of elements in the array
pin_array = list(map(int,input().split()))

# Calculate cumulative sum for each element
cumulative_sums = [cumulative_sum(num) for num in pin_array]

# Replace odd numbers with alphabets
result = replace_odd_with_alphabet(cumulative_sums)

# Output the result
print(result)


"""
Input
6
14 18 6 548 46 78

Result
ei68a6
"""
