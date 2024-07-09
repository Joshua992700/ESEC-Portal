def reverse_vowels(s: str) -> str:
    vowels = 'aeiouAEIOU'
    s = list(s)  # Convert string to list for in-place modification
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    return ''.join(s)  # Convert list back to string

# Test cases
n = input()
print(reverse_vowels(n))
