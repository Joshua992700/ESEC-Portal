def time_conversion(s):
    components = s[:-2].split(":")
    hours, minutes, seconds = map(int, components)
    suffix = s[-2:]
    
    if suffix == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

q = int(input())
for _ in range(q):
    s = input()
    result = time_conversion(s)
    print(result)
