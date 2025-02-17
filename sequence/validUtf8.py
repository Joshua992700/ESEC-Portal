def validUtf8(data):
    count = 0  # Number of bytes remaining in the current UTF-8 character

    for num in data:
        byte = num & 0xFF  # Use only the least significant 8 bits

        if count == 0:  # Start of a new character
            if byte >> 7 == 0b0:  # 1-byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:  # 2-byte character (110xxxxx)
                count = 1
            elif byte >> 4 == 0b1110:  # 3-byte character (1110xxxx)
                count = 2
            elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
                count = 3
            else:
                return False  # Invalid leading byte
        else:  # Continuation byte (must be of the form 10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            count -= 1  # Decrease continuation count

    return count == 0  # Ensure no unfinished multi-byte character

# Test cases
s = eval(input())
print(str(validUtf8(s)).lower())

"""
(or)
def validUtf8(data):
    cnt = 0

    for num in data:
        byte = num & 0xFF

        if cnt == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                cnt = 1
            elif byte >> 4 == 0b1110:
                cnt = 2
            elif byte >> 3 == 0b11110:
                cnt = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            cnt -= 1

    return cnt == 0

s = eval(input())
print(str(validUtf8(s)).lower())
"""
