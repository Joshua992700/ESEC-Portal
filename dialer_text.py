def letter_combinations(digits):
    if not digits:
        return []
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', ''],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    output = []
    backtrack("", digits)
    return ' '.join(output)

digits = input()
if digits == "1":
  print("No Combinations of Strings")
else:
  print(letter_combinations(digits))
