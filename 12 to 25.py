h = int(input())
m = int(input())
s = int(input())
ampm = input()

if ampm == "pm" and h!= 12:
    h += 12
elif ampm == "am" and h == 12:
    h = 0

print(f"{h:02d}:{m:02d}:{s:02d}")
