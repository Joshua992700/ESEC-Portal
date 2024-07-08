def number_to_text(num):
    num_dict = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100: "hundred"
    }
    
    if num in num_dict:
        return num_dict[num]
    
    if num < 100:
        tens, ones = divmod(num, 10)
        return num_dict[tens * 10] + (num_dict[ones] if ones != 0 else "")
    
    return ""

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char in vowels)

def find_pairs_count(nums, target):
    pairs_count = 0
    num_set = set(nums)
    
    for num in nums:
        if target - num in num_set:
            pairs_count += 1
            num_set.remove(num)
            if target - num in num_set:
                num_set.remove(target - num)
    
    return pairs_count

def number_to_textual(num):
    textual = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    return "greater 100" if num > 100 else textual[num]

def process_input(n, nums):
    total_vowels = 0
    for num in nums:
        text = number_to_text(num)
        total_vowels += count_vowels(text)
    
    digit_d = total_vowels
    pairs_count = find_pairs_count(nums, digit_d)
    return number_to_textual(pairs_count)

n = int(input())
nums = list(map(int, input().split()))
result = process_input(n, nums)
print(result)
