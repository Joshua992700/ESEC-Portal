def letterCombinations(digits):
    # Mapping from digits to corresponding characters
    digit_to_char = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    if not digits:  # If digits string is empty
        return []
    
    if '1' in digits:  # If digits contain 1, no valid combinations
        return ["No Combination of Strings"]
    
    result = []
    
    def backtrack(index, current_combination):
        # If the current combination is of the same length as digits, add it to the result
        if index == len(digits):
            result.append(current_combination)
            return
        
        # Get the letters for the current digit
        digit = digits[index]
        for char in digit_to_char[digit]:
            # Recurse to the next digit
            backtrack(index + 1, current_combination + char)
    
    # Start backtracking from the first digit
    backtrack(0, "")
    
    return result

digits = input().strip()
combinations = letterCombinations(digits)

if combinations == ["No Combination of Strings"]:
    print("No Combination of Strings")
else:
    print(" ".join(combinations))
