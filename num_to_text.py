def number_to_text(n):
    # Mapping numbers to their textual representation
    num_to_text = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
        90: "ninety", 100: "hundred"
    }
    
    if n in num_to_text:
        return num_to_text[n]
    elif n < 100:
        tens, ones = divmod(n, 10)
        return num_to_text[tens * 10] + ('' if ones == 0 else num_to_text[ones])
    else:
        return "hundred"

def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text if char in vowels)

def num_to_textual(n):
    # Mapping numbers to their textual representation for result
    text_representation = [
        "zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty", "twenty-one",
        "twenty-two", "twenty-three", "twenty-four", "twenty-five",
        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine",
        "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four",
        "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine",
        "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five",
        "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty",
        "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five",
        "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine", "sixty",
        "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five",
        "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", "seventy",
        "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five",
        "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine", "eighty",
        "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five",
        "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine", "ninety",
        "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five",
        "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine", "hundred"
    ]
    return "greater 100" if n > 100 else text_representation[n]

def find_pairs(numbers, D):
    count = 0
    seen = set()
    for number in numbers:
        if D - number in seen:
            count += 1
        seen.add(number)
    return count

def main():
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))

    # Step 1: Calculate digit D
    digit_D = sum(count_vowels(number_to_text(n)) for n in numbers)

    # Step 2: Find all unordered pairs of numbers in the input list whose sum equals D
    count_pairs = find_pairs(numbers, digit_D)

    # Step 3: Convert the count of such pairs to its textual representation
    result = num_to_textual(count_pairs)

    print(result)

if __name__ == "__main__":
    main()
