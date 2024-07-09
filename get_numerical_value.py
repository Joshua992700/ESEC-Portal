def get_numerical_value(word):
    # Convert each letter to its corresponding numerical value and concatenate them
    return int(''.join(str(ord(char) - ord('a')) for char in word))

def is_sum_equal(firstWord, secondWord, targetWord):
    # Get the numerical values of the words
    first_value = get_numerical_value(firstWord)
    second_value = get_numerical_value(secondWord)
    target_value = get_numerical_value(targetWord)
    
    # Check if the sum of first and second word's values equals the target word's value
    return (first_value + second_value) == target_value

# Example usage
firstWord = input().strip()
secondWord = input().strip()
targetWord = input().strip()

result = is_sum_equal(firstWord, secondWord, targetWord)
print(str(result).lower())
