def count_vowels(num):
    num_to_word = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'ix', 7: 'even', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'ixteen', 17: 'eventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'ixty', 70: 'eventy', 80: 'eighty',
        90: 'ninety', 100: 'hundred'
    }
    word = num_to_word[num]
    vowels = 'aeiou'
    count = sum(1 for char in word if char in vowels)
    return count

def find_pairs(nums, D):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == D:
                count += 1
    return count

N = int(input())
nums = list(map(int, input().split()))
vowel_count = sum(count_vowels(num) for num in nums)
D = vowel_count
pairs_count = find_pairs(nums, D)
if pairs_count > 100:
    print("greater 100")
else:
    num_to_word = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'ix', 7: 'even', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'ixteen', 17: 'eventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'ixty', 70: 'eventy', 80: 'eighty',
        90: 'ninety', 100: 'hundred'
    }
    print(num_to_word[pairs_count])
