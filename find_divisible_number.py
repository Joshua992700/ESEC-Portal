def find_divisible_number(arr):
    # Iterate over each element in the array
    for num in arr:
        # Check if this number divides all other numbers in the array
        is_divisor = True
        for element in arr:
            if element % num != 0:
                is_divisor = False
                break
        # If it is a divisor for all elements, return it
        if is_divisor:
            return num
    # If no such number is found, return -1
    return -1

# Input the size of the array
n = int(input())

# Input the array elements
arr = list(map(int, input().split()))

# Find the number that divides all other numbers
result = find_divisible_number(arr)

# Output the result
print(result)
