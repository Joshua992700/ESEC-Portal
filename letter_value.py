def getNumericalValue(word):
    # Convert each character to its corresponding numerical value and concatenate
    return int("".join(str(ord(char) - ord('a')) for char in word))

def isSumEqual(firstWord, secondWord, targetWord):
    # Calculate the numerical values of the words
    firstValue = getNumericalValue(firstWord)
    secondValue = getNumericalValue(secondWord)
    targetValue = getNumericalValue(targetWord)
    
    # Check if the sum of firstValue and secondValue equals targetValue
    return firstValue + secondValue == targetValue

# Example usage
firstWord = input()
secondWord = input()
targetWord = input()

# Output: True
print(str(isSumEqual(firstWord, secondWord, targetWord)).lower())
