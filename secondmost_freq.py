s = input()

d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

freq_list = sorted(d.items(), key=lambda item: item[1], reverse=True)

if len(freq_list) < 2:
    print("No Second most frequent character")
else:
    second_most_freq = freq_list[1][1]
    second_most_chars = [char for char, freq in freq_list if freq == second_most_freq]
    
    print(f"Second most frequent character is {''.join(second_most_chars)}")
