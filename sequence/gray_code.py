def is_valid_gray_code(sequence):
    n = max(sequence).bit_length()  # Calculate n based on max value
    max_value = (1 << n) - 1  # 2^n - 1

    # Condition 1: All numbers should be in range [0, 2^n - 1]
    if any(num < 0 or num > max_value for num in sequence):
        return False

    # Condition 2: No duplicates
    if len(sequence) != len(set(sequence)):
        return False

    # Condition 3: Check if consecutive numbers differ by exactly one bit
    def hamming_distance(x, y):
        return bin(x ^ y).count('1')  # XOR and count 1s

    for i in range(len(sequence) - 1):
        if hamming_distance(sequence[i], sequence[i + 1]) != 1:
            return False

    # Condition 4: Check circular difference
    if hamming_distance(sequence[0], sequence[-1]) != 1:
        return False

    return True

# Test cases
s = eval(input())
print(str(is_valid_gray_code(s)).lower())
