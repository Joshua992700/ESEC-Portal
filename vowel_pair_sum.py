def number_to_text(n):
    num_to_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100: "hundred"
    }
    
    if n <= 20:
        return num_to_words[n]
    elif n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        return num_to_words[tens] + ('' if ones == 0 else ' ' + num_to_words[ones])
    elif n == 100:
        return num_to_words[100]

def count_vowels(text):
    return sum(1 for char in text if char in 'aeiou')

def count_pairs(numbers, target):
    count = 0
    seen = {}
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
            
    return count

n = int(input().strip())
numbers = list(map(int, input().strip().split()))
    
total_vowels = 0
    
for number in numbers:
    text_representation = number_to_text(number)
    total_vowels += count_vowels(text_representation)
    
D = total_vowels
pair_count = count_pairs(numbers, D)
    
if pair_count > 100:
    print("greater 100")
else:
    print(number_to_text(pair_count))
