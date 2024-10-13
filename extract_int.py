def extract_integers_from_string(S):
    result = []
    current_number = ""
    
    for char in S:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                result.append(current_number)
                current_number = ""
    
    if current_number:
        result.append(current_number)
    
    return " ".join(result)

T = int(input())
for _ in range(T):
    S = input()
    print(extract_integers_from_string(S))

"""
Input
2
ramsathsfghhd A-118, Sector-136, Uttar Pradesh-201305
1abc35de 99fgh, dd11

Output
118 136 201305
1 35 99 11
"""
