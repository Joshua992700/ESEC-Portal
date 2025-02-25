n = int(input())

l = (n & 0xF0) >> 4
r = (n & 0x0F) << 4

print(l|r)
