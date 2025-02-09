import re

def is_master_word(word):
    # Check if the first character is not a digit
    if word[0].isdigit():
        return "NO 0"
    
    # Check if the second character is not a vowel
    if len(word) < 2 or word[1].lower() in 'aeiou':
        # If the second character is a vowel, we will still try to find NUM1 and NUM2
        num1_match = re.search(r'(\d+)', word)
        num2_match = re.search(r'(\d+)(?=[\[\]{}])', word)
        
        num1 = int(num1_match.group(1)) if num1_match else 0
        num2 = int(num2_match.group(1)) if num2_match else 0
        
        return f"NO {num1 - num2}"
    
    # Use regex to match the pattern for a MASTER word
    pattern = r'^[^\d][^aeiou](\d+)([AEIOU]+)(\d+)([\[\]{}])$'
    match = re.match(pattern, word)
    
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(3))
        return f"YES {num1 + num2}"
    else:
        # If it doesn't match, we need to find NUM1 and NUM2
        num1_match = re.search(r'(\d+)', word)
        num2_match = re.search(r'(\d+)(?=[\[\]{}])', word)
        
        num1 = int(num1_match.group(1)) if num1_match else 0
        num2 = int(num2_match.group(1)) if num2_match else 0
        
        return f"NO {num1 - num2}"

# Test the specific input
s = input()
result = is_master_word(s)
print(result)
